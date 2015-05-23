from pandac.PandaModules import NodePath

from toffee.element.Element import Element


class NodeElement(Element):
    TAG = 'node'

    def __init__(self):
        Element.__init__(self)

        self.name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def readTml(self, toplevelData, root):
        self.name = root.attrib['name']

        for child, element in self.readChildren(root):
            element.readTml(toplevelData, child)

    def traverse(self, parent):
        nodePath = NodePath(self.name)
        nodePath.reparentTo(parent)

        for child in self.children:
            child.traverse(nodePath)
