from toffee.element.Element import Element


class MetaElement(Element):
    TAG = 'meta'

    def readTml(self, toplevelData, root):
        for key, value in root.attrib.items():
            toplevelData[key] = value
