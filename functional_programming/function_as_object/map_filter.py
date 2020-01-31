import operator

students = [('Jack', 10), ('Katie', 9), ('John', 6)]

print([(name, grade) for name, grade in students if grade > 7])


def grades_above_seven(student):
    _, grade = student
    return grade > 7


print(list(filter(grades_above_seven, students)))

print([name for name, grade in students if grade > 7])


def get_name(student):
    name, _ = student
    return name


print(list(map(get_name, filter(grades_above_seven, students))))

print(list(map(operator.itemgetter(0), filter(grades_above_seven, students))))
