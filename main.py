import csv
from abc import ABC, abstractmethod

# ========= ABSTRACT BASE CLASS ==========
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected

    @abstractmethod
    def get_info(self):
        pass

# ========= STUDENT CLASS ==========
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_info(self):
        course_names = ', '.join(course.name for course in self.courses)
        return f"Student ID: {self.student_id}\nName: {self.name}\nAge: {self._age}\nCourses: {course_names}"

# ========= INSTRUCTOR CLASS ==========
class Instructor(Person):
    def __init__(self, name, age, instructor_id, salary):
        super().__init__(name, age)
        self.instructor_id = instructor_id
        self._salary = salary
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_info(self):
        course_names = ', '.join(course.name for course in self.courses)
        return f"Instructor ID: {self.instructor_id}\nName: {self.name}\nAge: {self._age}\nSalary: {self._salary}\nCourses: {course_names}"

# ========= COURSE CLASS ==========
class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.instructor = None

    def assign_instructor(self, instructor):
        self.instructor = instructor
        instructor.assign_course(self)

# ========= DEPARTMENT CLASS ==========
class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.students = {}
        self.instructors = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor

    def get_summary(self):
        return f"Department: {self.name}\nStudents: {len(self.students)}\nInstructors: {len(self.instructors)}"

# ========= UNIVERSITY CLASS ==========
class University:
    def __init__(self, name):
        self.name = name
        self.departments = {}
        self.courses = {}

    def add_department(self, department):
        self.departments[department.dept_id] = department

    def add_course(self, course):
        self.courses[course.code] = course

    def get_student_by_id(self, student_id):
        for dept in self.departments.values():
            if student_id in dept.students:
                return dept.students[student_id]
        return None

    def get_instructor_by_id(self, instructor_id):
        for dept in self.departments.values():
            if instructor_id in dept.instructors:
                return dept.instructors[instructor_id]
        return None

# ========= AUTHENTICATION ==========
users = {
    'admin': 'admin123',
    'staff': 'staff123'
}

def authenticate():
    print("\n=== LOGIN ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

# ========= CSV SAVE FUNCTIONS ==========
def save_students_to_csv(departments):
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Name', 'Age', 'Courses'])
        for dept in departments.values():
            for student in dept.students.values():
                courses = ', '.join(course.name for course in student.courses)
                writer.writerow([student.student_id, student.name, student._age, courses])

def save_instructors_to_csv(departments):
    with open('instructors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Instructor ID', 'Name', 'Age', 'Salary', 'Courses'])
        for dept in departments.values():
            for instructor in dept.instructors.values():
                courses = ', '.join(course.name for course in instructor.courses)
                writer.writerow([instructor.instructor_id, instructor.name, instructor._age, instructor._salary, courses])

# ========= MENU SYSTEM ==========
def main_menu():
    if not authenticate():
        return

    university = University("RealTech University")

    while True:
        print("\n==== UNIVERSITY MANAGEMENT SYSTEM ====")
        print("1. Add Department")
        print("2. Add Student")
        print("3. Add Instructor")
        print("4. Add Course")
        print("5. Assign Instructor to Course")
        print("6. Register Student in Course")
        print("7. View Student by ID")
        print("8. View Department Summary")
        print("9. View Instructor by ID")
        print("10. Save Data to CSV Files")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            dept_id = input("Enter department ID: ")
            name = input("Enter department name: ")
            dept = Department(dept_id, name)
            university.add_department(dept)
            print("Department added.")

        elif choice == '2':
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            student_id = input("Enter student ID: ")
            dept_id = input("Enter department ID: ")
            student = Student(name, age, student_id)
            if dept_id in university.departments:
                university.departments[dept_id].add_student(student)
                print("Student added to department.")
            else:
                print("Department not found.")

        elif choice == '3':
            name = input("Enter instructor name: ")
            age = int(input("Enter age: "))
            instructor_id = input("Enter instructor ID: ")
            salary = float(input("Enter salary: "))
            dept_id = input("Enter department ID: ")
            instructor = Instructor(name, age, instructor_id, salary)
            if dept_id in university.departments:
                university.departments[dept_id].add_instructor(instructor)
                print("Instructor added to department.")
            else:
                print("Department not found.")

        elif choice == '4':
            name = input("Enter course name: ")
            code = input("Enter course code: ")
            course = Course(name, code)
            university.add_course(course)
            print("Course added.")

        elif choice == '5':
            code = input("Enter course code: ")
            instructor_id = input("Enter instructor ID: ")
            course = university.courses.get(code)
            instructor = None
            for dept in university.departments.values():
                if instructor_id in dept.instructors:
                    instructor = dept.instructors[instructor_id]
            if course and instructor:
                course.assign_instructor(instructor)
                print("Instructor assigned.")
            else:
                print("Invalid course or instructor ID.")

        elif choice == '6':
            student_id = input("Enter student ID: ")
            code = input("Enter course code: ")
            student = university.get_student_by_id(student_id)
            course = university.courses.get(code)
            if student and course:
                student.register_course(course)
                print("Student registered to course.")
            else:
                print("Invalid student ID or course code.")

        elif choice == '7':
            student_id = input("Enter student ID to view: ")
            student = university.get_student_by_id(student_id)
            if student:
                print("\n--- Student Details ---")
                print(student.get_info())
            else:
                print("Student not found.")

        elif choice == '8':
            for dept in university.departments.values():
                print(dept.get_summary())

        elif choice == '9':
            instructor_id = input("Enter instructor ID to view: ")
            instructor = university.get_instructor_by_id(instructor_id)
            if instructor:
                print("\n--- Instructor Details ---")
                print(instructor.get_info())
            else:
                print("Instructor not found.")

        elif choice == '10':
            save_students_to_csv(university.departments)
            save_instructors_to_csv(university.departments)
            print("Data saved to CSV files.")

        elif choice == '11':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# ========= ENTRY POINT ==========
if __name__ == "__main__":
    main_menu()
