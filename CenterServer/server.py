from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from CenterServer.Protocols import protocol
from Libs import const


class GateFactory(ReconnectingClientFactory):
    protocol = protocol.GateProtocol
    gateProto = None
    matchTask = None
    matchList = []

    roomDict = {}
    roomTask = None

    def clientConnectionFailed(self, connector, reason):
        if self.matchTask:
            self.matchTask.stop()
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)

    def clientConnectionLost(self, connector, reason):
        if self.matchTask:
            self.matchTask.stop()
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def update(self):
        for key, value in self.roomDict.items():
            value.update(const.UpdateTimeInterval)


def startGateFactory(config):
    gateIP = config.get('center_server').get("gate_address").get('host')
    gatePort = config.get('center_server').get("gate_address").get('port')

    global GateInstance
    GateInstance = GateFactory()
    reactor.connectTCP(gateIP, gatePort, GateInstance)
    print("Center Server Start!")
