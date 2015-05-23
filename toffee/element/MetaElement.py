from toffee.element.Element import Element

import collections

from xml.etree import ElementTree


class MetaElement(Element):
    TAG = 'meta'

    def __init__(self):
        Element.__init__(self)

        self.meta = collections.OrderedDict()

    def readTml(self, toplevelData, root):
        for key, value in root.attrib.items():
            self.meta[key] = value
            toplevelData[key] = value

    def writeTml(self, parent):
        meta = ElementTree.SubElement(parent, self.TAG, **self.meta)
