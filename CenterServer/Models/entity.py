

class Entity():
    entityID = 0
    modelID = 0
    speed = 0
    rotation = [0, 0, 0]
    position = [0, 0, 0]
    health = 100

    def __init__(self, ID):
        self.entityID = ID

    def update(self, timeInterval):
        pass