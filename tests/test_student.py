from models.student import Student

def test_student_creation():
    s = Student("Saqib", 20, "S101")
    assert s.name == "Saqib"
    assert s.roll_number == "S101"
