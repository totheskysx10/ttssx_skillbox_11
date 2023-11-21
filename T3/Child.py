class Child:
    def __init__(self, name, age, calm_state=True, hunger_state=True):
        self.name = name
        self.age = age
        self.calm_state = calm_state
        self.hunger_state = hunger_state

    def set_calm_state(self, state):
        self.calm_state = state

    def set_hunger_state(self, state):
        self.hunger_state = state