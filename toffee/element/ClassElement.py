from toffee.element.Element import Element
from toffee.element import ClassPool

from xml.etree import ElementTree


class ClassElement(Element):
    TAG = 'class'

    def __init__(self):
        Element.__init__(self)

        self.rel = None
        self.name = None
        self.attributes = None

    def setRel(self, rel):
        self.rel = rel

    def getRel(self):
        return self.rel

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getAttributes(self):
        return self.attributes

    def readTml(self, toplevelData, root):
        self.rel = root.attrib.pop('rel')
        self.name = root.attrib.pop('name')
        self.attributes = root.attrib.copy()

        ClassPool.addClass(self.rel, self.name, self.attributes.copy())

    def writeTml(self, parent):
        class_ = ElementTree.SubElement(parent, self.TAG, rel=self.rel,
                                        name=self.name, **self.attributes)

    def cleanup(self):
        ClassPool.removeClass(self.rel, self.name)

        del self.rel
        del self.name

        self.attributes.clear()
        del self.attributes

        Element.cleanup(self)
