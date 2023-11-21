import random
from Warrior import Warrior

class Program:
    @staticmethod
    def main():
        first = Warrior()
        second = Warrior()

        while not first.is_dead() and not second.is_dead():
            case = random.randint(0, 1)
            if case == 0:
                second.damage(first.get_power())
                print(f"Атаковал первый юнит. У второго юнита осталось {second.get_health()} здоровья")
            elif case == 1:
                first.damage(second.get_power())
                print(f"Атаковал второй юнит. У первого юнита осталось {first.get_health()} здоровья")

        print(f"Одержал победу {'первый' if second.is_dead() else 'второй'} юнит")

if __name__ == '__main__':
    Program.main()