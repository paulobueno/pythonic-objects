from functools import wraps
from time import sleep, strftime
from decorator import decorator, getfullargspec


# def get_time(fn=None, *, tms='%H:%M:%S'):
#     if fn is not None:
#         return get_time(tms='%H:%M:%S')(fn)
#
#     def decorator(f):
#         @wraps(f)
#         def insert_time(*args, **kwargs):
#             print(strftime(tms))
#             return f(*args, **kwargs)
#
#         return insert_time
#
#     return decorator

@decorator
def get_time(f, tms='%H:%M:%S', *args, **kwargs):
    print(strftime(tms))
    return f(*args, **kwargs)


@get_time
def number():
    return 10


@get_time(tms='%D %T')
def hello_name(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    print(getfullargspec(number))
    print(number())
    print(getfullargspec(hello_name))
    print(hello_name('Paulo'))
    print(hello_name.__name__)
    sleep(1)
    print(number())
    print(hello_name('Joao'))
    print(hello_name.__name__)
