class Warrior:
    def __init__(self) -> None:
        self.health = 100
        self.power = 20

    def damage (self, amount):
        self.health -= amount

    def is_dead(self):
        return self.health <= 0

    def get_power(self):
        return self.power

    def get_health(self):
        return self.health