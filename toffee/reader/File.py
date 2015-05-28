from toffee.core.Error import ToffeeError

from toffee.toplevel.ToplevelData import ToplevelData
from toffee.toplevel.Toplevel import Toplevel


class File:
    def __init__(self, path):
        self.path = path
        self.toplevelData = None
        self.toplevel = None

    def getToplevel(self):
        return self.toplevel

    def getToplevelData(self):
        return self.toplevelData

    def generateToplevelData(self):
        if self.toplevelData is not None:
            raise ToffeeError('Tried to load toplevel data more than once.')

        self.toplevelData = ToplevelData()

        if self.path.endswith('.tml'):
            self.toplevelData.readTml(self.path)
        elif self.path.endswith('.tof'):
            self.toplevelData.readTof(self.path)
        else:
            raise ToffeeError('Invalid file type: ' + self.path)

        return self.toplevelData

    def generateToplevel(self):
        if self.toplevelData is None:
            raise ToffeeError('Tried to generate toplevel with no data.')

        if self.toplevel is not None:
            raise ToffeeError('Tried to generate toplevel more than once.')

        self.toplevel = Toplevel(self.toplevelData)
        self.toplevel.traverse()

        return self.toplevel
