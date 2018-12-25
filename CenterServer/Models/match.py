from CenterServer.Models import room
from Libs import const
from CenterServer import server
import copy
import time


def handleWaiters():
    waiters = server.GateInstance.matchList
    if len(waiters) <= 0:
        return
    waitersCache = copy.deepcopy(waiters)
    length = len(waitersCache)
    roomDict = server.GateInstance.roomDict
    for key, value in roomDict.items():
        left = const.RoomMemMax - len(value.members)
        if left > 0:
            minvalue = min(left, len(waitersCache))
            value.addPlayers(waitersCache[:minvalue])
            del waitersCache[:minvalue]

    while len(waitersCache) > 0:
        minvalue = min(len(waitersCache), const.RoomMemMax)
        roomid = int(time.time())
        house = room.Room(str(roomid))
        house.addPlayers(waitersCache[:minvalue])
        del waitersCache[:minvalue]
        roomDict[house.roomID] = house
    del waiters[:length]
