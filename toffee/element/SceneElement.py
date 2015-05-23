from pandac.PandaModules import NodePath

from toffee.element.Element import Element
from toffee.element import ElementPool


class SceneElement(Element):
    TAG = 'scene'

    def __init__(self):
        Element.__init__(self)

        self.name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def readTml(self, toplevelData, root):
        self.name = root.attrib['name']

        for child in root:
            element = ElementPool.createElement(child.tag)
            self.addChild(element)
            element.readTml(toplevelData, child)

    def traverse(self):
        nodePath = NodePath(self.name)

        for child in self.children:
            child.traverse(nodePath)

        return nodePath
