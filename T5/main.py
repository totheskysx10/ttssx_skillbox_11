import random

class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 20
        self.house.food -= 20

    def work(self):
        self.satiety -= 10
        self.house.money += 50

    def play(self):
        self.satiety -= 10

    def go_shopping(self):
        self.house.food += 30
        self.satiety -= 10
        self.house.money -= 30

    def live_one_day(self):
        dice_roll = random.randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice_roll == 1:
            self.work()
        elif dice_roll == 2:
            self.eat()
        else:
            self.play()

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

house = House()
person1 = Person("Artem", house)
person2 = Person("Alice", house)

for day in range(365):
    print(f"День {day + 1}:")
    person1.live_one_day()
    person2.live_one_day()
    print(f"{person1.name}: Сытость - {person1.satiety}, Деньги - {house.money}, Еда - {house.food}")
    print(f"{person2.name}: Сытость - {person2.satiety}, Деньги - {house.money}, Еда - {house.food}")
    print()

print("Результат:")
print(f"{person1.name}: Сытость - {person1.satiety}, Деньги - {house.money}, Еда - {house.food}")
print(f"{person2.name}: Сытость - {person2.satiety}, Деньги - {house.money}, Еда - {house.food}")
