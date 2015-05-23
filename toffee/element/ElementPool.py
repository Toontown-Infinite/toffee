from toffee.error.Error import ToffeeSyntaxError


elements = {}


def createElement(tag):
    if tag not in elements:
        raise ToffeeSyntaxError('Non-existent element: ' + tag)

    element = elements[tag]()
    return element


def addElement(element):
    if element.TAG in elements:
        raise ToffeeSyntaxError('Multiple elements with tag: ' + element.TAG)

    elements[element.TAG] = element
