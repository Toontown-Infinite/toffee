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

    def readTml(self, toplevelData, root):
        self.src = root.attrib.get('src')

        NodeElement.readTml(self, toplevelData, root)

    def applyAttributes(self, nodePath):
        NodeElement.applyAttributes(self, nodePath)

        nodePath.setName(self.name)

    def traverse(self, parent):
        model = loader.loadModel(self.src)
        self.applyAttributes(model)
        model.reparentTo(parent)

        for child in self.children:
            child.traverse(model)

    def cleanup(self):
        del self.src

        NodeElement.cleanup(self)
