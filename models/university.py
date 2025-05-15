class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

    def show_departments(self):
        for d in self.departments:
            print(d.summary())
