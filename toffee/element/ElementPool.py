from toffee.error.Error import ToffeeElementError


elements = {}


def getElementCtor(tag):
    if tag not in elements:
        raise ToffeeElementError('Non-existent element: ' + tag)

    return elements


def addElementCtor(ctor):
    if ctor.TAG in elements:
        raise ToffeeElementError('Multiple elements with tag: ' + ctor.TAG)

    elements[ctor.TAG] = ctor
