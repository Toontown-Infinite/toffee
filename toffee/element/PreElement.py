from toffee.element.Element import Element


class PreElement(Element):
    TAG = 'pre'
    VALID_CHILDREN = ['include', 'class', 'meta']

    def readTml(self, toplevelData, root):
        for child, element in self.readChildren(root):
            element.readTml(toplevelData, child)
