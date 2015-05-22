from toffee.reader.File import File


def readToffeeFile(filepath):
    toffeeFile = File(filepath)
    scene = toffeeFile.generateScene()
    return scene
