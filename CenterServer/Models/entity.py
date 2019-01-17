

class Entity():
    entityID = ""
    modelID = 0
    speed = 0
    rotation = [0, 0, 0]
    position = [0, 0, 0]
    health = 100
    healthMax = 100
    score = 0

    def __init__(self, ID):
        self.entityID = ID

    def update(self, timeInterval):
        pass
