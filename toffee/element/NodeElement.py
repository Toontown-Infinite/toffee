from pandac.PandaModules import NodePath

from toffee.element.Element import Element


class NodeElement(Element):
    TAG = 'node'
    VALID_CHILDREN = ['node', 'model']

    def __init__(self):
        Element.__init__(self)

        self.name = None
        self.xyz = []
        self.hpr = []
        self.scale = []
        self.color = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setXyz(self, x, y, z):
        self.xyz = [x, y, z]

    def getXyz(self):
        return self.xyz

    def setHpr(self, h, p, r):
        self.hpr = [h, p, r]

    def getHpr(self):
        return self.hpr

    def setScale(self, x, y, z):
        self.scale = [x, y, z]

    def getScale(self):
        return self.scale

    def setColor(self, r, g, b, a):
        self.color = [r, g, b, a]

    def getColor(self):
        return self.color

    def readTml(self, toplevelData, root):
        self.name = root.attrib.get('name')

        xyz = root.attrib.get('xyz', '0 0 0')
        xyz = xyz.split()

        for value in xyz:
            self.xyz.append(float(value))

        hpr = root.attrib.get('hpr', '0 0 0')
        hpr = hpr.split()

        for value in hpr:
            self.hpr.append(float(value))

        scale = root.attrib.get('scale', '1 1 1')
        scale = scale.split()

        for value in scale:
            self.scale.append(float(value))

        color = root.attrib.get('color', '1 1 1 1')
        color = color.split()

        for value in color:
            self.color.append(float(value))

        Element.readTml(self, toplevelData, root)

    def applyAttributes(self, nodePath):
        nodePath.setPos(*self.xyz)
        nodePath.setHpr(*self.hpr)
        nodePath.setColor(*self.color)
        nodePath.setScale(*self.scale)

    def traverse(self, parent):
        nodePath = NodePath(self.name)
        self.applyAttributes(nodePath)
        nodePath.reparentTo(parent)

        for child in self.children:
            child.traverse(nodePath)
