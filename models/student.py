from .person import Person

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.courses = []

    def register_course(self, course):
        self.courses.append(course)

    def get_info(self):
        return f"Student: {self.name}, Age: {self._age}, Roll#: {self.roll_number}"
