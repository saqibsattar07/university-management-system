import csv
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent / "data"

def save_students(students):
    with open(data_dir / "students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Roll Number", "Courses"])
        for student in students.values():
            courses = ";".join([c.name for c in student.courses])
            writer.writerow([student.name, student._age, student.roll_number, courses])

def save_instructors(instructors):
    with open(data_dir / "instructors.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Instructor ID", "Salary", "Courses"])
        for instr in instructors.values():
            courses = ";".join([c.name for c in instr.courses])
            writer.writerow([instr.name, instr._age, instr.instructor_id, instr._salary, courses])
