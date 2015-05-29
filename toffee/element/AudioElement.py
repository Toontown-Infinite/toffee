from toffee.element.Element import Element
from toffee.attribute.AudioAttribute import AudioAttribute


class AudioElement(Element):
    TAG = 'audio'

    def __init__(self):
        Element.__init__(self)

        self.src = None
        self.volume = None

    def readTml(self, toplevelData, root):
        self.src = root.attrib['src']
        self.volume = float(root.attrib.get('volume', '1'))

        Element.readTml(self, toplevelData, root)

    def traverse(self, toplevel, parent):
        attribute = AudioAttribute()
        attribute.construct(self.src, self.volume, parent)

        toplevel.addAttribute(attribute)
