from os.path import abspath, dirname, join, normpath


def enum(**enums):
    return type('Enum', (), enums)


PREFIX = normpath(dirname(abspath(__file__)))
AppPath = join(PREFIX, r'../')

UserPrefix = "user"
TokenDict = "tokens"

RoomMemMax = 100
MoveSpeed = 10
ShootCD = 0.4

MatchTimeInterval = 1
UpdateTimeInterval = 0.1

Config = enum(
    Map="Map",
)
