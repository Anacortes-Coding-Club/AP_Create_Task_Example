class ComponentSystem:
    def __init__(self):
        self.components = {}

    def add_component(self, game_object, component):
        if game_object not in self.components:
            self.components[game_object] = []
        self.components[game_object].append(component)

    def remove_component(self, game_object, component):
        if game_object in self.components:
            self.components[game_object].remove(component)

    def get_components(self, game_object):
        return self.components.get(game_object, [])

    def update_components(self, game_object):
        if game_object in self.components:
            for component in self.components[game_object]:
                component.update()