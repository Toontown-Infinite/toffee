class Element:
    TAG = 'element'

    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def readTof(self, toplevelData):
        pass

    def readTml(self, toplevelData, root):
        pass
