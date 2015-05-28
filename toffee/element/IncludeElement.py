from xml.etree import ElementTree

from toffee.element.Element import Element
from toffee.core import Constants
from toffee.core.Error import ToffeeIncludeError, ToffeePluginError


class IncludeElement(Element):
    TAG = 'include'

    def __init__(self):
        Element.__init__(self)

        self.rel = None
        self.src = None

    def setRel(self, rel):
        self.rel = rel

    def getRel(self):
        return self.rel

    def setSrc(self, src):
        self.src = src

    def getSrc(self):
        return self.src

    def readTml(self, toplevelData, root):
        self.rel = root.attrib['rel']
        self.src = root.attrib['src']

        if self.rel == Constants.REL_TML:
            toplevelData.readTml(self.src)
        elif self.rel == Constants.REL_TOF:
            toplevelData.readTof(self.src)
        elif self.rel == Constants.REL_PLUGIN:
            try:
                __import__('plugins.' + self.src)
            except ImportError:
                raise ToffeePluginError('Error loading plugin: ' + self.src)
        else:
            raise ToffeeIncludeError('Invalid relationship: ' + self.rel)

    def writeTml(self, parent):
        include = ElementTree.SubElement(parent, self.TAG,
                                         rel=self.rel, src=self.src)

    def cleanup(self):
        del self.rel
        del self.src

        Element.cleanup(self)