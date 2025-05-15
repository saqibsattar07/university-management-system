class Course:
    course_count = 0

    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.instructor = None
        Course.course_count += 1

    @classmethod
    def total_courses(cls):
        return cls.course_count

    def assign_instructor(self, instructor):
        self.instructor = instructor
        instructor.assign_course(self)
