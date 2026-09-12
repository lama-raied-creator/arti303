"""Student record utilities for ARTI 303."""


class Student:
    """A single student record."""

    def __init__(self, name, age, gpa, is_enrolled=True):
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")

        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self):
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5
    
    def report_line(self):
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"

def average_gpa(students):
    if not students:
        return 0.0

    total = 0.0

    for student in students:
        total += student.gpa

    return total / len(students)    
def dean_list_students(students):
    result = []

    for student in students:
        if student.is_dean_list():
            result.append(student)

    return result
def letter_grade(gpa):
    if gpa >= 3.7:
        return "A"
    elif gpa >= 2.7:
        return "B"
    elif gpa >= 1.7:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"
def oldest_student(students):
    if not students:
        raise ValueError("Student list cannot be empty")

    oldest = students[0]

    for student in students[1:]:
        if student.age > oldest.age:
            oldest = student

    return oldest
def group_by_enrollment(students):
    enrolled = []
    not_enrolled = []

    for student in students:
        if student.is_enrolled:
            enrolled.append(student)
        else:
            not_enrolled.append(student)

    return enrolled, not_enrolled
def students_above_gpa(students, minimum_gpa):
    """Return students whose GPA is greater than or equal to minimum_gpa."""
    result = []

    for student in students:
        if student.gpa >= minimum_gpa:
            result.append(student)

    return result