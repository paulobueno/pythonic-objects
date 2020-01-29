"""
>>> def hello():
...    print('hello')
...
>>> execute(hello)
hello
>>> execute(hello,2)
hello
hello
>>> execute(hello,3)
hello
hello
hello
"""


def execute(f, n=1):
    for _ in range(n):
        f()
