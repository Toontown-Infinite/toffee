from xml.etree import ElementTree

from toffee.scene.Metadata import Metadata
from toffee.element import ElementPool


class SceneData:
    def __init__(self):
        self.metadata = Metadata()
        self.elements = []

    def readTof(self, path):
        pass

    def readTml(self, path):
        tree = ElementTree.parse(path)
        root = tree.getroot()

        for child in root:
            element = ElementPool.createElement(child.tag)
            self.elements.append(element)
            element.readTml(self, child)
