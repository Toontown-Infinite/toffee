from toffee.core.Error import ToffeeAttributeError


class Attribute:
    def construct(self):
        raise ToffeeAttributeError(
            'Attribute ' + self.__class__.__name__ + 'has no construct method')

    def destroy(self):
        raise ToffeeAttributeError(
            'Attribute ' + self.__class__.__name__ + 'has no destroy method')
