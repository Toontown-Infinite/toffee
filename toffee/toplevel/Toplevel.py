from pandac.PandaModules import NodePath


class Toplevel(NodePath):
    def __init__(self, toplevelData):
        NodePath.__init__(self, 'toplevel')

        self.toplevelData = toplevelData

    def traverse(self):
        for element in self.toplevelData.getToplevelElements():
            nodePath = element.traverse()
            if nodePath is not None:
                nodePath.reparentTo(self)

        return self
