class ToffeeError(Exception):
    pass


class ToffeeSyntaxError(ToffeeError):
    pass


class ToffeeIncludeError(ToffeeError):
    pass


class ToffeeClassError(ToffeeError):
    pass


class ToffeePluginError(ToffeeError):
    pass


class ToffeeAttributeError(ToffeeError):
    pass
