from pandac.PandaModules import NodePath


class Toplevel(NodePath):
    def __init__(self, toplevelData):
        NodePath.__init__(self, 'toplevel')

        self.toplevelData = toplevelData

    def traverse(self):
        for element in self.toplevelData.getToplevelElements():
            element.traverse(self)

        return self
