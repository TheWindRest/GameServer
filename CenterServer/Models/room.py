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
                entityID = str(key1 + 1) + "_" + str(key2 + 1)
                item = entity.Entity(entityID)
                item.position = [key1, key2, 0]
                item.modelID = value2
                line.append(item)
            self.entitys.append(line)

    def addPlayers(self, players):
        for _, value in enumerate(players):
            userInfo = user.getUser(value)
            if userInfo is None:
                continue
            userInfo["roomid"] = self.roomID
            user.updateUser(userInfo, ["roomid"])
            self.members[value] = player.Player(value, userInfo["name"])
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
            target = self.entitys[int(x) - 1][int(y) - 1]
        member.score += 10
        target.health -= 10

        msg.damage = 10
        self.broadcastMsg(msg)
        self.broadcastState(member, CS_GS_pb2.Entity_Active)
        self.broadcastState(target, msg.target.entitytype)

    def update(self, timeInterval):
        msgInfo = CS_GS_pb2.TransformSync()
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
        msgInfo.roomid = self.roomID
        zipMsg = CS_GS_pb2.TransmitMsg()
        zipMsg.msgid = msgInfo.msgid
        for key, value in self.members.items():
            if not value.active:
                continue
            zipMsg.mail = key
            msgInfo.mail = key
            self.gateProto.transmitMessage(zipMsg, msgInfo)

    def broadcastState(self, member, entityType):
        msgInfo = CS_GS_pb2.StateSync()
        msgInfo.entity.entitytype = entityType
        msgInfo.entity.entityid = member.entityID
        msgInfo.entity.health = member.health
        msgInfo.entity.score = member.score
        self.broadcastMsg(msgInfo)
