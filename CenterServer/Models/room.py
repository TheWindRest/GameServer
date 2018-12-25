from CenterServer import server
from Libs.protobuf import CS_GS_pb2
from CenterServer.Models import player
import copy
import time
from Libs import const
from CenterServer.Models import user


class Room():
    roomID = 0
    members = {}
    gateProto = None

    def __init__(self, ID):
        self.roomID = ID
        self.gateProto = server.GateInstance.gateProto

    def addPlayers(self, players):
        for key, value in enumerate(players):
            self.members[value] = player.Player(value)
            userInfo = user.getUser(value)
            if userInfo:
                userInfo["roomid"] = self.roomID
                user.updateUser(userInfo, ["roomid"])
            zipMsg = CS_GS_pb2.TransmitMsg()
            zipMsg.mail = value
            msgInfo = CS_GS_pb2.EnterRoom()
            msgInfo.mail = value
            msgInfo.name = "test"
            msgInfo.roomid = self.roomID
            self.gateProto.transmitMessage(zipMsg, msgInfo)

    def deletePlayer(self, mail):
        if self.members.get(mail):
            self.members.pop(mail)
            print("delete player:", mail)

    def transformSync(self, msg):
        member = self.members.get(msg.mail)
        if member:
            member.active = True
            transformInfo = msg.transforminfo[0]
            member.speed = transformInfo.speed
            member.position = copy.deepcopy(transformInfo.position)
            member.rotation = copy.deepcopy(transformInfo.rotation)

    def shootBullet(self, msg):
        member = self.members.get(msg.mail)
        if member is None:
            return
        if member.lastShootTime + const.ShootCD > time.time():
            return
        member.lastShootTime = time.time()

    def update(self, timeInterval):
        msgInfo = CS_GS_pb2.TransformSync()
        msgInfo.roomid = self.roomID
        for key, value in self.members.items():
            if not value.active:
                continue
            value.update(timeInterval)

            transformInfo = msgInfo.transforminfo.add()
            transformInfo.mail = key
            transformInfo.speed = value.speed
            for key, pos in enumerate(value.position):
                transformInfo.position.append(pos)
            for key, rot in enumerate(value.rotation):
                transformInfo.rotation.append(rot)

        self.broadcastMsg(msgInfo)

    def broadcastMsg(self, msgInfo):
        zipMsg = CS_GS_pb2.TransmitMsg()
        zipMsg.msgid = msgInfo.msgid
        for key, value in self.members.items():
            if not value.active:
                continue
            zipMsg.mail = key
            msgInfo.mail = key
            self.gateProto.transmitMessage(zipMsg, msgInfo)
