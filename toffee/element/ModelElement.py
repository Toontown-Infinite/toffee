from toffee.element.NodeElement import NodeElement


class ModelElement(NodeElement):
    TAG = 'model'

    def __init__(self):
        NodeElement.__init__(self)

        self.src = None

    def setSrc(self, src):
        self.src = src

    def getSrc(self):
        return self.src

    def traverse(self, parent):
        model = loader.loadModel(self.src)
        model.reparentTo(parent)

        for child in self.children:
            child.traverse(model)
