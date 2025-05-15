from .person import Person

class Instructor(Person):
    def __init__(self, name, age, salary, instructor_id):
        super().__init__(name, age)
        self._salary = salary
        self.instructor_id = instructor_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_info(self):
        return f"Instructor: {self.name}, Age: {self._age}, Salary: {self._salary}"
