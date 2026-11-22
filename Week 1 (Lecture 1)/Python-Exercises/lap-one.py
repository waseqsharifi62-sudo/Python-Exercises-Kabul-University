from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.email}"

class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self):
        return f"Student: {self.student_id}"

    def __str__(self):
        return f"{super().__str__()} - ID: {self.student_id}"

class Lecturer(Person):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

    def role_info(self):
        return f"Lecturer: {self.employee_id}"

    def __str__(self):
        return f"{super().__str__()} - ID: {self.employee_id}"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.course_name}"