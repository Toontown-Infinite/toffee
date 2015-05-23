import collections

import itertools

from xml.etree import ElementTree

from toffee.error.Error import ToffeeSyntaxError
from toffee.element import ElementPool


class ToplevelData(collections.MutableMapping):
    def __init__(self):
        self.meta = collections.OrderedDict()
        self.elements = collections.OrderedDict()

    def getToplevelElements(self):
        return tuple(itertools.chain(*self.elements.values()))

    def readTof(self, path):
        pass

    def readTml(self, path):
        elements = []

        tree = ElementTree.parse(path)
        root = tree.getroot()

        for child in root:
            element = ElementPool.createElement(child.tag)

            if child.tag not in ('pre', 'node'):
                raise ToffeeSyntaxError('Invalid child "%s" for root "%s"' %
                                        (child.tag, root.tag))

            elements.append(element)
            element.readTml(self, child)

        self.elements[path] = elements

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
