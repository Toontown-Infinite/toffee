from toffee.error.Error import ToffeeSyntaxError
from toffee.element import ElementPool
from toffee.element import ClassPool


class Element:
    TAG = ''
    VALID_CHILDREN = []

    def __init__(self):
        self.children = []

    def addChild(self, child):
        if child.TAG not in self.VALID_CHILDREN:
            raise ToffeeSyntaxError('Invalid child "%s" for root "%s"' %
                                    (child.TAG, self.TAG))

        self.children.append(child)

    def getChildren(self):
        return self.children

    def readTof(self, toplevelData):
        pass

    def readTml(self, toplevelData, root):
        if 'class' in root.attrib:
            attributes = ClassPool.getClass(self.TAG, root.attrib['class'])
            self.__dict__.update(attributes)

        for child in root:
            element = ElementPool.createElement(child.tag)
            self.addChild(element)
            element.readTml(toplevelData, child)

    def traverse(self, parent):
        pass
