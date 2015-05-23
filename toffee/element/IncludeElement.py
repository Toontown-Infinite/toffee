from toffee.element.Element import Element
from toffee.core import Constants
from toffee.error.Error import ToffeeIncludeError


class IncludeElement(Element):
    TAG = 'include'

    def readTml(self, toplevelData, root):
        rel = root.attrib['rel']
        src = root.attrib['src']

        if rel == Constants.REL_TML:
            toplevelData.readTml(src)
        elif rel == Constants.REL_TOF:
            toplevelData.readTof(src)
        else:
            raise ToffeeIncludeError('Invalid relationship: ' + rel)
