from models.student import Student
from models.instructor import Instructor
from models.course import Course
from services.data_manager import save_students, save_instructors

students = {}
instructors = {}

def run_menu():
    while True:
        print("\\n===== University Management System =====")
        print("1. Add Student")
        print("2. View Student by ID")
        print("3. Add Instructor")
        print("4. View Instructor by ID")
        print("5. Save Data to CSV")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            roll = input("Roll Number: ")
            students[roll] = Student(name, age, roll)
            print("✅ Student added.")
        elif choice == '2':
            roll = input("Enter Roll Number: ")
            student = students.get(roll)
            if student:
                print(student.get_info())
            else:
                print("❌ Student not found.")
        elif choice == '3':
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            instructor_id = input("Instructor ID: ")
            instructors[instructor_id] = Instructor(name, age, salary, instructor_id)
            print("✅ Instructor added.")
        elif choice == '4':
            instructor_id = input("Enter Instructor ID: ")
            instructor = instructors.get(instructor_id)
            if instructor:
                print(instructor.get_info())
            else:
                print("❌ Instructor not found.")
        elif choice == '5':
            save_students(students)
            save_instructors(instructors)
            print("💾 Data saved to CSV.")
        elif choice == '0':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")
