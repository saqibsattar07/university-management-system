from models.instructor import Instructor

def test_instructor_creation():
    i = Instructor("Yemna", 35, 50000, "I101")
    assert i.name == "Yemna"
    assert i._salary == 50000
    assert i.instructor_id == "I101"
