from functional_programming.decorator.marker import get_marked, mark


def first():
    pass


mark(first)

@mark
def second():
    pass


if __name__ == '__main__':
    for _ in get_marked():
        print(_.__name__)
