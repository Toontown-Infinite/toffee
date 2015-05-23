from pandac.PandaModules import NodePath

from toffee.element.Element import Element


class NodeElement(Element):
    TAG = 'node'
    VALID_CHILDREN = ['node', 'model']

    def __init__(self):
        Element.__init__(self)

        self.name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def readTml(self, toplevelData, root):
        self.name = root.attrib.get('name', 'node')

        Element.readTml(self, toplevelData, root)

    def traverse(self, parent):
        nodePath = NodePath(self.name)
        nodePath.reparentTo(parent)

        for child in self.children:
            child.traverse(nodePath)
