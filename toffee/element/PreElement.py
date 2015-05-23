from toffee.element.Element import Element


class PreElement(Element):
    TAG = 'pre'

    def readTml(self, toplevelData, root):
        for child, element in self.readChildren(root):
            element.readTml(toplevelData, child)
