class RegistrationError(Exception):
    pass

class CourseFullError(RegistrationError):
    pass

class Course:
    def __init__(self, code, capacity):
        self.code = code
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.capacity:
            raise CourseFullError(f"{self.code} is full")
        self.students.append(student)

def register(student, course):
    try:
        course.add_student(student)
        print(f"Registered {student}")
    except CourseFullError as e:
        print(f"Error: {e}")

course = Course("CS101", 1)
register("Ali", course)
register("Sara", course)