from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.python import log
from twisted.python.logfile import DailyLogFile

import os

from LoginServer.Protocols import protocol


class ClientFactory(ServerFactory):
    protocol = protocol.ClientProtocol
    users = {}
    offlineUsers = {}

    def __init__(self, config):
        self.logPath = config.get("log_path")
        assert self.logPath

    def startFactory(self):
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        log_name = r'login_server.log'
        log.startLogging(DailyLogFile(log_name, self.logPath))

        super().startFactory()
        print("Login-Client-Listener Start!")

    def stopFactory(self):
        print("Login-Client-Listener Stop!")
        super().stopFactory()


class GateFactory(ServerFactory):
    protocol = protocol.GateProtocol
    gateServers = {}
    gateAddrs = {}

    def __init__(self, config):
        self.gateAddrs = config.get("login_server").get("gate_address")
        assert(self.gateAddrs)

    def startFactory(self):
        print("Login-Gate-Listener Start!")
        super().startFactory()

    def stopFactory(self):
        print("Login-Gate-Listener Stop!")
        super().stopFactory()

    def getSmallestServer(self):
        _, gate = min(self.gateServers.items(), key=lambda x: x[1].gateInfo["players"])
        return gate.gateInfo


def startClientFactory(config):
    clientIP = config.get('login_server').get("client_listen").get('host')
    clientPort = config.get('login_server').get("client_listen").get('port')

    global ClinetInstance
    ClinetInstance = ClientFactory(config)
    reactor.listenTCP(clientPort, ClinetInstance, interface=clientIP)


def startGateFactory(config):
    gateIP = config.get('login_server').get("gate_listen").get('host')
    gatePort = config.get('login_server').get("gate_listen").get('port')

    global GateInstance
    GateInstance = GateFactory(config)
    reactor.listenTCP(gatePort, GateInstance, interface=gateIP)
