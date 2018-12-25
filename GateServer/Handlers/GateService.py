from twisted.python import log
from Libs.protobuf import GC_GS_pb2, GS_LS_pb2, CS_GS_pb2
from Libs import error
import time
from GateServer import server
import uuid


def createUUID():
    return uuid.uuid1().__str__()


# Clinet<-->Gate
def sendErrorMsg(p, errorid):
    assert(type(errorid) == int)
    msg = GC_GS_pb2.ErrorMsg()
    msg.errorid = errorid
    p.sendMessage(msg)


def process_user_login(p, body):
    msgInfo = GC_GS_pb2.TokenLogin()
    msgInfo.ParseFromString(body)
    log.msg("recv msg:" + msgInfo.__str__())

    if msgInfo.token == "":
        loginProto = server.LoginInstance.loginProto
        if loginProto:
            p.factory.waiters[msgInfo.mail] = p
            checkInfo = GS_LS_pb2.CheckLogin()
            checkInfo.mail = msgInfo.mail
            checkInfo.password = msgInfo.password
            checkInfo.result = 0
            loginProto.sendMessage(checkInfo)
    else:
        token = p.factory.tokenDict.get(msgInfo.mail)
        if token is None:
            sendErrorMsg(p, error.ERR_CHECK_LOGIN)
            p.transport.loseConnection()
        elif token.get("token") == msgInfo.token:
            oldUser = p.factory.users.get(msgInfo.mail)
            if oldUser:
                p.factory.users.pop(msgInfo.mail)
                sendErrorMsg(error.ERR_LOGIN_OTHER)
                oldUser.transport.loseConnection()

            token = createUUID()
            p.factory.tokenDict[msgInfo.mail] = {
                "token": token,
                "liveTime": int(time.time()) + 3600
            }
            p.factory.users[msgInfo.mail] = p
            p.userInfo = {
                "mail": msgInfo.mail
            }
            msgInfo = GC_GS_pb2.TokenLogin()
            msgInfo.token = token
            p.sendMessage(msgInfo)
        elif token.get("token") != msgInfo.token:
            sendErrorMsg(p, error.ERR_CHECK_LOGIN)
            p.transport.loseConnection()


# Gate<-->Login
def process_register_result(p, body):
    msgInfo = GS_LS_pb2.AskRegister()
    msgInfo.ParseFromString(body)
    log.msg("recv msg:" + msgInfo.__str__())

    if msgInfo.state == 1:
        p.factory.loginProto = p
        log.msg("Gate Register Success!")


def process_check_result(p, body):
    checkInfo = GS_LS_pb2.CheckLogin()
    checkInfo.ParseFromString(body)
    log.msg("recv msg:" + checkInfo.__str__())

    waiter = server.ClinetInstance.waiters.get(checkInfo.mail)
    if waiter is None:
        return

    if checkInfo.result:
        oldUser = server.ClinetInstance.users.get(checkInfo.mail)
        if oldUser:
            server.ClinetInstance.users.pop(checkInfo.mail)
            sendErrorMsg(oldUser, error.ERR_LOGIN_OTHER)
            oldUser.transport.loseConnection()

        token = createUUID()
        server.ClinetInstance.tokenDict[checkInfo.mail] = {
            "token": token,
            "liveTime": int(time.time()) + 3600
        }
        server.ClinetInstance.users[checkInfo.mail] = waiter
        waiter.userInfo = {
            "mail": checkInfo.mail
        }
        server.ClinetInstance.waiters.pop(checkInfo.mail)
        msgInfo = GC_GS_pb2.TokenLogin()
        msgInfo.token = token
        waiter.sendMessage(msgInfo)
    else:
        waiter.factory.waiters.pop(checkInfo.mail)
        sendErrorMsg(waiter, error.ERR_CHECK_LOGIN)
        waiter.transport.loseConnection()


# Center<-->Gate
def process_center_register(p, body):
    msgInfo = CS_GS_pb2.AskRegister()
    msgInfo.ParseFromString(body)
    log.msg("recv msg:" + msgInfo.__str__())

    centerHost = p.transport.getPeer().host
    if centerHost in p.factory.centerAddrs.keys():
        if centerHost in p.factory.centerServers.keys():
            gate, _ = p.factory.centerServers.get(centerHost)
            p.factory.centerServers.pop(centerHost)
            gate.transport.loseConnection()

        msgList = []
        for key, value in enumerate(msgInfo.msgList):
            msgList.append(int(value))

        p.factory.centerServers[centerHost] = (p, msgList)

        log.msg("Center<%s> Register!" % centerHost)
        msgInfo.state = 1

        transmitMsg = CS_GS_pb2.TransmitMsg()
        transmitMsg.mail = ""
        transmitMsg.msgid = msgInfo.msgid
        transmitMsg.data = msgInfo.SerializeToString()
        p.sendMessage(transmitMsg)
    else:
        msg = CS_GS_pb2.ErrorMsg()
        msg.errorid = error.ERR_CENTER_ADDRESS
        transmitMsg = CS_GS_pb2.TransmitMsg()
        transmitMsg.mail = ""
        transmitMsg.msgid = msg.msgid
        transmitMsg.data = msg.SerializeToString()
        p.sendMessage(msg)
        p.transport.loseConnection()
