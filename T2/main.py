import random

from Student import Student


class Program:
    @staticmethod
    def main():

        students_list = [
            Student("Alice Smith", "1", [random.uniform(2, 5) for _ in range(5)]),
            Student("Bob Johnson", "2", [random.uniform(2, 5) for _ in range(5)]),
            Student("Charlie Davis", "3", [random.uniform(2, 5) for _ in range(5)]),
            Student("David Brown", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Eva Miller", "5", [random.uniform(2, 5) for _ in range(5)]),
            Student("Frank Wilson", "6", [random.uniform(2, 5) for _ in range(5)]),
            Student("Grace Taylor", "7", [random.uniform(2, 5) for _ in range(5)]),
            Student("Hank Harris", "8", [random.uniform(2, 5) for _ in range(5)]),
            Student("Ivy Robinson", "9", [random.uniform(2, 5) for _ in range(5)]),
            Student("Jack White", "10", [random.uniform(2, 5) for _ in range(5)]),
        ]

        students_list.sort(key=lambda rate: rate.get_average_grade())

        print("\n".join(map(str, students_list)))

if __name__ == '__main__':
    Program.main()