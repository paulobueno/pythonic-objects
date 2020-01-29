students = [('Jack', 10), ('Katie', 9), ('John', 6)]

students.sort(key=lambda student: student[1])
print(students)


def name_sort(student):
    return student[0]


print(sorted(students, key=name_sort))
