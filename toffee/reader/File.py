from toffee.error.Error import ToffeeError

from toffee.scene.SceneData import SceneData


class File:
    def __init__(self, path):
        self.path = path
        self.sceneData = None
        self.scene = None

    def generateSceneData(self):
        if self.sceneData is not None:
            raise ToffeeError('Tried to load scene data more than once.')

        self.sceneData = SceneData()

        if self.path.endswith('.tml'):
            self.sceneData.readTml(self.path)
        elif self.path.endswith('.tof'):
            self.sceneData.readTof(self.path)
        else:
            raise ToffeeError('Invalid file type: ' + self.path)

        return self.sceneData

    def generateScene(self):
        if self.sceneData is None:
            raise ToffeeError('Tried to generate scene with no data.')
