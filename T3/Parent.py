class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.age} лет.")
        if self.children:
            print("У меня есть дети:")
            for child in self.children:
                print(f"- {child.name}")

    def comfort_child(self, child):
        print(f"{self.name} успокаивает {child.name}.")
        child.set_calm_state(True)

    def feed_child(self, child):
        print(f"{self.name} кормит {child.name}.")
        child.set_hunger_state(False)
