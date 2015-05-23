import collections

import itertools

from xml.etree import ElementTree

from toffee.error.Error import ToffeeError, ToffeeSyntaxError
from toffee.element import ElementPool


class ToplevelData(collections.MutableMapping):
    def __init__(self):
        self.meta = collections.OrderedDict()
        self.elements = collections.OrderedDict()

    def getToplevelElements(self):
        return tuple(itertools.chain(*self.elements.values()))

    def readTof(self, path):
        pass

    def writeTof(self):
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

    def writeTml(self, file, path):
        if file not in self.elements:
            raise ToffeeError('Unknown file: ' + file)

        elements = self.elements[file]

        root = ElementTree.Element('tml')

        for element in elements:
            element.writeTml(root)

        ToplevelData.formatTml(root)

        tree = ElementTree.ElementTree(root)
        tree.write(path)

    @staticmethod
    def formatTml(element, level=0):
        indent = "\n" + level * "    "

        if len(element):
            if not element.text or not element.text.strip():
                element.text = indent + "    "
            if not element.tail or not element.tail.strip():
                element.tail = indent
            for element in element:
                ToplevelData.formatTml(element, level+1)
            if not element.tail or not element.tail.strip():
                element.tail = indent
        else:
            if level and (not element.tail or not element.tail.strip()):
                element.tail = indent

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
