def myDecorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling testFunc {args}, {kwargs}')
        a = func(*args, **kwargs)
        print(f'Finished testFunc {a}')
    return wrapper


@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)
    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)