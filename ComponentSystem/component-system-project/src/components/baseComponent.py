class BaseComponent:
    def __init__(self):
        pass

    def update(self):
        pass

    def initialize(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"