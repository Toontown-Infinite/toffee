from toffee.element.Element import Element


class PreElement(Element):
    TAG = 'pre'
    VALID_CHILDREN = ['include', 'class', 'meta']
