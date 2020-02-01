def num_counter():
    _counter = 0

    def adding():
        nonlocal _counter
        _counter += 1
        return _counter

    return adding


test_count1 = num_counter()
test_count2 = num_counter()
print(test_count1())
print(test_count1())
print(test_count2())
print(test_count2())
print(test_count2())
