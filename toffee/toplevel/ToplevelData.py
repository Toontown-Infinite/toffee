import collections

from xml.etree import ElementTree

from toffee.error.Error import ToffeeSyntaxError
from toffee.element.PreElement import PreElement
from toffee.element.NodeElement import NodeElement
from toffee.element import ElementPool


class ToplevelData(collections.MutableMapping):
    def __init__(self):
        self.meta = {}
        self.elements = []

    def getToplevelElements(self):
        return self.elements

    def readTof(self, path):
        pass

    def readTml(self, path):
        tree = ElementTree.parse(path)
        root = tree.getroot()

        for child in root:
            element = ElementPool.createElement(child.tag)

            if not isinstance(element, (PreElement, NodeElement)):
                raise ToffeeSyntaxError('Invalid child "%s" for root "%s"' % (child.tag, root.tag))

            self.elements.append(element)
            element.readTml(self, child)

    def get(self, item, default=None):
        return self.meta.get(item, default)

    def __setitem__(self, key, value):
        self.meta[key] = value

    def __getitem__(self, item):
        return self.meta[item]

    def __delitem__(self, key):
        del self.meta[key]

    def __len__(self):
        return len(self.meta)

    def __iter__(self):
        return iter(self.meta)
