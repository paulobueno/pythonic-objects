from functools import wraps
from time import sleep, strftime


def get_time(tms='%H:%M:%S'):
    def decorator(f):
        @wraps(f)
        def insert_time(*args, **kwargs):
            print(strftime(tms))
            return f(*args, **kwargs)

        return insert_time

    return decorator


@get_time()
def number():
    return 10


@get_time(tms='%D %T')
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
