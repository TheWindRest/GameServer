from struct import pack, unpack, calcsize
from twisted.protocols.policies import TimeoutMixin
from twisted.python import log
from twisted.internet.protocol import Protocol
from traceback import print_exc
from twisted.python.log import theLogPublisher
import errno


class ParseProtocol:
    _lengthBaseFormat = 'i'
    _sendFormat = 'ii'
    _delimLength = calcsize(_lengthBaseFormat)

    REQUEST_HANDLERS = {
    }

    def __init__(self):
        self.buf = b''

    def decodeData(self, data):
        self.buf += data
        while True:
            buffer_length = len(self.buf)
            if buffer_length < self._delimLength:
                return
            bodylength = unpack(self._lengthBaseFormat, self.buf[:4])[0]
            msgID = unpack(self._lengthBaseFormat, self.buf[4:8])[0]
            if buffer_length < bodylength:
                return
            buf = self.buf[8:bodylength]
            self.buf = self.buf[bodylength:]
            self.handleMessage(msgID, buf)

    def handleMessage(self, msgID, Data):
        handler = self.REQUEST_HANDLERS.get(msgID)
        if handler:
            handler(self, Data)
        else:
            if getattr(self.factory, "handleMessage", None):
                self.factory.handleMessage(self, msgID, Data)
            else:
                print("handle not found:%i" % msgID)

    def encodeData(self, msgID, body):
        bytesData = body.SerializeToString()
        packData = pack(self._sendFormat, len(bytesData) + 8, msgID) + bytesData
        return packData

    def packData(self, msgID, body):
        packData = pack(self._sendFormat, len(body) + 8, msgID) + body
        return packData


class GoogleProtocol(Protocol, TimeoutMixin, ParseProtocol):
    def dataReceived(self, data):
        self.decodeData(data)

    def sendMessage(self, body):
        log.msg("send msg:" + body.__str__())
        data = self.encodeData(body.msgid, body)
        self.sendBytes(data)

    def sendBytes(self, bytesData):
        if bytesData is None:
            return
        counter = 0
        while True:
            try:
                self.transport.getHandle().sendall(bytesData)
                break
            except Exception as e:
                print_exc()
                if e.errno == errno.EAGAIN:
                    print("Send Again")
                    continue
                    counter += 1
                    if counter >= 10:
                        break
                else:
                    break

    def connectionMade(self):
        theLogPublisher.msg('new client linked.', self.transport.getPeer())

    def connectionLost(self, reason):
        theLogPublisher.msg('[%s] Connection lost. reason:' % self.__class__.__name__, reason.getErrorMessage())
