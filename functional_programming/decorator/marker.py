_marked = []


def get_marked():
    return _marked


def mark(f):
    global _marked
    _marked.append(f)
    return f
