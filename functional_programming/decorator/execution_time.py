from functools import wraps
from time import sleep, strftime


def get_time(f):
    @wraps(f)
    def insert_time(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return insert_time


@get_time
def number():
    return 10


@get_time
def hello_name(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    print(number())
    print(hello_name('Paulo'))
    print(hello_name.__name__)
    sleep(1)
    print(number())
    print(hello_name('Joao'))
    print(hello_name.__name__)
