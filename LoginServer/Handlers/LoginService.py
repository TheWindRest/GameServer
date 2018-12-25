from twisted.python import log
from Libs.protobuf import GC_LS_pb2, GS_LS_pb2
from LoginServer.Models import user
from Libs import error
from LoginServer import server


# Clinet<-->Login
def sendErrorMsg(p, errorid):
    assert(type(errorid) == int)
    msg = GC_LS_pb2.ErrorMsg()
    msg.errorid = errorid
    p.sendMessage(msg)


def process_user_login(p, body):
    msgInfo = GC_LS_pb2.AskLogin()
    msgInfo.ParseFromString(body)
    log.msg("recv msg:" + msgInfo.__str__())

    userData = user.getUserByMail(msgInfo.mail, msgInfo.password)
    if userData is None:
        return sendErrorMsg(p, error.ERR_LOGIN_FAILED)

    mail = userData.get("mail")
    oldUser = p.factory.users.get(mail)
    if oldUser:
        p.factory.users.pop(mail)
        sendErrorMsg(error.ERR_LOGIN_OTHER)
        oldUser.transport.loseConnection()

    p.userInfo = {
        "mail": mail,
    }
    p.factory.users[mail] = p
    if mail in p.factory.offlineUsers.keys():
        p.factory.offlineUsers.pop(mail)
    log.msg("Player<%s> Login!" % userData.get("name"))

    gate = server.GateInstance.getSmallestServer()
    msgInfo = GC_LS_pb2.ServerBSAddr()
    gateServer = msgInfo.serverinfo.add()
    gateServer.ServerName = gate["name"]
    gateServer.ServerAddr = gate["host"]
    gateServer.ServerPort = gate["port"]
    gateServer.ServerState = 1
    p.sendMessage(msgInfo)


# Gate<-->Login
def process_gate_register(p, body):
    msgInfo = GS_LS_pb2.AskRegister()
    msgInfo.ParseFromString(body)
    log.msg("recv msg:" + msgInfo.__str__())

    gateHost = p.transport.getPeer().host
    if gateHost in p.factory.gateAddrs.keys():
        gate = p.factory.gateServers.get(gateHost)
        if gate:
            p.factory.gateServers.pop(gateHost)
            gate.transport.loseConnection()

        p.factory.gateServers[gateHost] = p
        p.gateInfo = {
            "name": p.factory.gateAddrs[gateHost],
            "host": msgInfo.host,
            "port": msgInfo.port,
            "players": 0,
        }
        log.msg("Gate<%s> Register!" % gateHost)
        msgInfo.state = 1
        p.sendMessage(msgInfo)
    else:
        msg = GS_LS_pb2.ErrorMsg()
        msg.errorid = error.ERR_GATE_ADDRESS
        p.sendMessage(msg)
        p.transport.loseConnection()


def process_check_login(p, body):
    checkInfo = GS_LS_pb2.CheckLogin()
    checkInfo.ParseFromString(body)
    log.msg("recv msg:" + checkInfo.__str__())

    userData = user.getUser(checkInfo.mail)
    if userData is None:
        checkInfo.result = 0
        return p.sendMessage(checkInfo)
    else:
        inLine = checkInfo.mail in server.ClinetInstance.offlineUsers.keys()
        inDatabase = userData["password"] == checkInfo.password
        checkInfo.result = 1 if inLine and inDatabase else 0
        return p.sendMessage(checkInfo)
