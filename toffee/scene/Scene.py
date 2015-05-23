from pandac.PandaModules import NodePath


class Scene(NodePath):
    def __int__(self, sceneData):
        NodePath.__init__(self)

        self.sceneData = sceneData
