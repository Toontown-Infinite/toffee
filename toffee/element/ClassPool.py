import collections

from toffee.error.Error import ToffeeClassError


classes = collections.OrderedDict()


def addClass(rel, name, attributes):
    if rel not in classes:
        classes[rel] = collections.OrderedDict()

    if name in classes[rel]:
        raise ToffeeClassError('Class already defined: ' + name)

    classes[rel][name] = attributes


def removeClass(rel, name):
    if rel not in classes:
        raise ToffeeClassError('Unknown relationship: ' + rel)

    if name not in classes[rel]:
        raise ToffeeClassError('Unknown class "%s" for relationship "%"' %
                               (name, rel))

    classes[rel][name].clear()
    del classes[rel][name]


def getClass(rel, name):
    if rel not in classes:
        raise ToffeeClassError('Unknown relationship: ' + rel)

    if name not in classes[rel]:
        raise ToffeeClassError('Unknown class "%s" for relationship "%"' %
                               (name, rel))

    return classes[rel][name]
