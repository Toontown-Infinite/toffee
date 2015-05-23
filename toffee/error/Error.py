class ToffeeError(Exception):
    pass


class ToffeeSyntaxError(ToffeeError):
    pass


class ToffeeIncludeError(ToffeeError):
    pass


class ToffeeClassError(ToffeeError):
    pass
