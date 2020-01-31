def func_test():
    def new_func():
        return 10
    return new_func

func_test_1=func_test()
func_test_2=func_test()
print(func_test_1 is func_test_2)
print(func_test_1)
print(func_test_2)