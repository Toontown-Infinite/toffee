from toffee.error.Error import ToffeeSyntaxError

from toffee.element import ElementPool


class Element:
    TAG = ''
    VALID_CHILDREN = []

    def __init__(self):
        self.children = []

    def addChild(self, child):
        if not isinstance(child, self.VALID_CHILDREN):
            raise ToffeeSyntaxError('Invalid child "%s" for root "%s"' %
                                    (child.TAG, self.TAG))

        self.children.append(child)

    def getChildren(self):
        return self.children

    def readTof(self, toplevelData):
        pass

    def readTml(self, toplevelData, root):
        pass

    def readChildren(self, root):
        for child in root:
            element = ElementPool.createElement(child.tag)
            self.addChild(element)
            yield child, element

    def traverse(self, parent):
        pass
