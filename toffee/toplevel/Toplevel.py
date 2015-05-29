from panda3d.core import NodePath


class Toplevel(NodePath):
    def __init__(self, toplevelData):
        NodePath.__init__(self, 'toplevel')

        self.toplevelData = toplevelData
        self.attributes = []

    def addAttribute(self, attribute):
        self.attributes.append(attribute)

    def destroy(self):
        for attribute in self.attributes:
            attribute.destroy()

        self.removeNode()

    def traverse(self):
        for element in self.toplevelData.getToplevelElements():
            element.traverse(self, self)

        return self
