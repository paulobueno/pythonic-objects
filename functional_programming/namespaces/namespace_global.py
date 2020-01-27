a = 1


def f(a=3):
    print(a)
    print(globals())
    print(locals())


class A:
    a = 9
    a += 30
    print(a)
    print(globals())
    print(locals())


f()
