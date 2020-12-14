def print_result(func, *arg):
    def decor(*arg):
        print(func.__name__)
        a=func(*arg)
        if type(a) is list:
            for k  in a:
                print(k)
        elif type(a) is dict:
            for k, v in a.items():
                print(k,'=',v)
        else:
            print(a)
        return a
    return decor

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__=='__main__':
   test_1()
   test_2()
   test_3()
   test_4()
