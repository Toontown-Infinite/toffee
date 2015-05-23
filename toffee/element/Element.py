class Element:
    TAG = 'element'

    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def tof(self):
        pass

    def tml(self):
        pass
