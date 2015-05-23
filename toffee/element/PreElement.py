from toffee.element.Element import Element
from toffee.element import ElementPool


class PreElement(Element):
    TAG = 'pre'

    def readTml(self, sceneData, root):
        for child in root:
            element = ElementPool.createElement(child.tag)
            self.addChild(element)
            element.readTml(sceneData, child)
