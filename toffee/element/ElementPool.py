from toffee.error.Error import ToffeeElementError


elements = {}


def createElement(tag):
    if tag not in elements:
        raise ToffeeElementError('Non-existent element: ' + tag)

    element = elements[tag]()
    return element


def addElement(element):
    if element.TAG in elements:
        raise ToffeeElementError('Multiple elements with tag: ' + element.TAG)

    elements[element.TAG] = element
