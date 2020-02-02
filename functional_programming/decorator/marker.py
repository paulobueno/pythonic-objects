_marked = []


def get_marked():
    return _marked


def mark(f):
    _marked.append(f)
    return f
