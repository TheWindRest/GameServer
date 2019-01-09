from os.path import join, normpath
from Libs import const
from CenterServer import db_redis


def getMapData(mapID):
    mapTable = db_redis.getTable(const.Config.Map)
    mapName = mapTable[str(mapID)]["Name"]
    filePath = join(const.AppPath, r'Libs/map/MapInfo' + str(mapName) + r"_Level1.bytes")
    with open(normpath(filePath), 'r') as f:
        content = f.read()
        mapArray = []
        for line in f.readlines():
            lineArray = [value for value in line.split(',')]
            mapArray.append(lineArray)
        return content, mapArray
