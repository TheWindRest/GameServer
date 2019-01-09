from CenterServer import server
from Libs.protobuf import CS_GS_pb2
from CenterServer.Models import entity
from CenterServer.Models import player
import copy
import time
from Libs import const
from CenterServer.Models import user
from CenterServer.Models import map_data


class Room():
    entityBaseID = 0
    roomID = 0
    mapID = 0
    mapData = ""
    mapArray = []
    members = {}
    entitys = []
    gateProto = None

    def __init__(self, ID, mapID=1):
        self.roomID = ID
        self.mapID = mapID
        self.mapData, self.mapArray = map_data.getMapData(mapID)
        self.gateProto = server.GateInstance.gateProto

        for key1, value1 in enumerate(self.mapArray):
            line = []
            for key2, value2 in enumerate(value1):
                self.entityBaseID += 1
                item = entity.Entity(self.entityBaseID)
                item.position = [key1, key2, 0]
                item.modelID = value2
                line.append(item)
            self.entitys.append(line)

    def addPlayers(self, players):
        for _, value in enumerate(players):
            userInfo = user.getUser(value)
            if userInfo is None:
                continue
            self.entityBaseID += 1
            userInfo["roomid"] = self.roomID
            user.updateUser(userInfo, ["roomid"])
            self.members[value] = player.Player(self.entityBaseID, value, userInfo["name"])
            zipMsg = CS_GS_pb2.TransmitMsg()
            zipMsg.mail = value
            msgInfo = CS_GS_pb2.EnterRoom()
            msgInfo.mail = value
            msgInfo.name = userInfo["name"]
            msgInfo.roomid = self.roomID
            msgInfo.mapid = str(self.mapID)
            msgInfo.mapdata = self.mapData
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
        member.bullet -= 1
        self.broadcastMsg(msg)

    def takeDamage(self, msg):
        member = self.members.get(msg.mail)
        target = None
        if msg.target.entitytype == CS_GS_pb2.Entity_Active:
            target = self.members.get(msg.target.entityid)
        elif msg.target.entitytype == CS_GS_pb2.Entity_Static:
            x, y = msg.target.entityid.split('_')
            target = self.entitys[int(x)][int(y)]
        member.score += 10
        target.health -= 10

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
