from toffee.error.Error import ToffeeError


class File:
    def __init__(self, path):
        self.path = path
        self.sceneData = None
        self.scene = None

    def generateSceneData(self):
        if self.sceneData is not None:
            raise ToffeeError('Tried to load scene data more than once.')

    def generateScene(self):
        if self.sceneData is None:
            raise ToffeeError('Tried to generate scene with no data.')
