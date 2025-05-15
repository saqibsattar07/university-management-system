class Department:
    def __init__(self, dept_id, name):
        self.__id = dept_id
        self.name = name
        self.students = []
        self.instructors = []

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def summary(self):
        return f"Department: {self.name}, Students: {len(self.students)}, Instructors: {len(self.instructors)}"
