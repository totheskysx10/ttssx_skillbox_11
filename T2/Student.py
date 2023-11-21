class Student:
    def __init__(self, name_surname: str, group_id: str, grades: list[float]):
        self.grades = grades
        self.group_id = group_id
        self.name_surname = name_surname

    def __str__(self):
        return f"Student: {self.name_surname}. Group Id: {self.group_id}. Grades: {self.grades}"

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)