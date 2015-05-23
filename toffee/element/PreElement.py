from toffee.element.Element import Element
from toffee.element import ElementPool


class PreElement(Element):
    TAG = 'pre'

    def readTml(self, toplevelData, root):
        for child in root:
            element = ElementPool.createElement(child.tag)
            self.addChild(element)
            element.readTml(toplevelData, child)
