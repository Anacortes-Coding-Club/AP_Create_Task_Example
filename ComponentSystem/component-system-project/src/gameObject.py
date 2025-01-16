class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.components = {}

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def add_component(self, name, component):
        self.components[name] = component

    def remove_component(self, name):
        if name in self.components:
            del self.components[name]

    def get_component(self, name):
        return self.components.get(name)

    def __repr__(self):
        return f"GameObject(x={self.x}, y={self.y}, width={self.width}, height={self.height}, components={self.components})"