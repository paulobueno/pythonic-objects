students = [ ('Jack', 10), ('Katie', 9), ('John', 6) ]

print([ (name, grade) for name, grade in students if grade > 7 ])


def grades_above_seven(student):
    _, grade = student
    return grade > 7


print(list(filter(grades_above_seven, students)))
