from toffee.element.Element import Element

from xml.etree import ElementTree


class PreElement(Element):
    TAG = 'pre'
    VALID_CHILDREN = ['include', 'class', 'meta']

    def writeTml(self, parent):
        pre = ElementTree.SubElement(parent, self.TAG)

        for child in self.children:
            child.writeTml(pre)
