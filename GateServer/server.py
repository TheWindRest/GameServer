from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, ReconnectingClientFactory
from twisted.python import log
from twisted.python.logfile import DailyLogFile
from Libs import error

import os

from GateServer.Protocols import protocol
from Libs.protobuf import CS_GS_pb2


class ClientFactory(ServerFactory):
    protocol = protocol.ClientProtocol
    users = {}
    tokenDict = {}
    waiters = {}

    def __init__(self, config):
        self.logPath = config.get("log_path")
        assert self.logPath

    def startFactory(self):
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        log_name = r'gate_server.log'
        log.startLogging(DailyLogFile(log_name, self.logPath))

        super().startFactory()
        print("Client->Gate-Listener Start!")

    def stopFactory(self):
        print("Client->Gate-Listener Stop!")
        super().stopFactory()

    def handleMessage(self, proto, msgID, Data):
        for key, value in CenterInstance.centerServers.items():
            centerProto, msgList = value
            if msgID in msgList:
                transmitMsg = CS_GS_pb2.TransmitMsg()
                transmitMsg.mail = proto.userInfo.get("mail")
                transmitMsg.msgid = msgID
                transmitMsg.data = Data
                return centerProto.sendMessage(transmitMsg)

        print("handle not found:%i" % msgID)


class LoginFactory(ReconnectingClientFactory):
    protocol = protocol.LoginProtocol
    loginProto = None
    listenIP = ""
    listenPort = 0

    def __init__(self, config):
        self.listenIP = config.get('gate_server').get("client_listen").get('host')
        self.listenPort = config.get('gate_server').get("client_listen").get('port')

    def clientConnectionFailed(self, connector, reason):
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)

    def clientConnectionLost(self, connector, reason):
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)


class CenterFactory(ServerFactory):
    centerServers = {}
    protocol = protocol.CenterProtocol
    centerAddrs = {}

    def __init__(self, config):
        self.centerAddrs = config.get("gate_server").get("center_address")
        assert(self.centerAddrs)

    def startFactory(self):
        super().startFactory()
        print("Center->Gate-Listener Start!")

    def stopFactory(self):
        super().stopFactory()
        print("Center->Gate-Listener Stop!")

    def handleMessage(self, proto, msgID, Data):
        transmitMsg = CS_GS_pb2.TransmitMsg()
        transmitMsg.ParseFromString(Data)
        mail = transmitMsg.mail
        bytesDdata = transmitMsg.data

        user = ClinetInstance.users.get(mail)
        if user:
            packData = user.packData(msgID, bytesDdata)
            user.sendBytes(packData)
        else:
            transmitMsg = CS_GS_pb2.TransmitMsg()
            transmitMsg.mail = mail
            transmitMsg.msgid = CS_GS_pb2.GS2CS_Error
            errorMsg = CS_GS_pb2.ErrorMsg()
            errorMsg.errorid = error.ERR_USER_LOGOUT
            transmitMsg.data = errorMsg.SerializeToString()
            proto.sendMessage(transmitMsg)
            print("cant find user:", mail, msgID)


def startClientFactory(config):
    clientIP = config.get('gate_server').get("client_listen").get('host')
    clientPort = config.get('gate_server').get("client_listen").get('port')
    global ClinetInstance
    ClinetInstance = ClientFactory(config)
    reactor.listenTCP(clientPort, ClinetInstance, interface=clientIP)


def startCenterFactory(config):
    clientIP = config.get('gate_server').get("center_listen").get('host')
    clientPort = config.get('gate_server').get("center_listen").get('port')
    global CenterInstance
    CenterInstance = CenterFactory(config)
    reactor.listenTCP(clientPort, CenterInstance, interface=clientIP)


def startLoginFactory(config):
    loginIP = config.get('gate_server').get("login_address").get('host')
    loginPort = config.get('gate_server').get("login_address").get('port')

    global LoginInstance
    LoginInstance = LoginFactory(config)
    reactor.connectTCP(loginIP, loginPort, LoginInstance)
