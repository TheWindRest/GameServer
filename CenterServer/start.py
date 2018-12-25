from twisted.internet import reactor
from twisted.python import log
from twisted.python.logfile import DailyLogFile
import argparse
import json
import os

from CenterServer import server
from CenterServer import db_redis


def readConfig(configFile):
    fin = open(configFile, 'r', encoding="utf-8")
    return json.load(fin)


def startLog(configFile):
    logPath = configFile.get("log_path")
    assert logPath
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    log_name = r'center_server.log'
    log.startLogging(DailyLogFile(log_name, logPath))


parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, default='../config.json', help='config file')
parser.add_argument('--name', type=str, help='server')

args = parser.parse_args()
configInfo = readConfig(args.cfg)

startLog(configInfo)
db_redis.initRedis(configInfo)
server.startGateFactory(configInfo)
reactor.run()
