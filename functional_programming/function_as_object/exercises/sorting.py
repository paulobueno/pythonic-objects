"""
The goal of this exercise is to create a function that sort by grade and then by name
a list of tuples containing (name, grade)
>>> students = [('Renzo', 0), ('Luciano', 10), ('Renzo Santos', 10), ('Renzo Nuccitelli', 10)]
>>> students.sort(key=sort_grade_name)
>>> students
[('Renzo', 0), ('Luciano', 10), ('Renzo Nuccitelli', 10), ('Renzo Santos', 10)]
"""


def sort_grade_name(student):
    name, grade = student
    return grade, name
