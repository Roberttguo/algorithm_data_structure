def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

def my_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

@my_decorator
def myfunction(x):
    print(f"With argument '{x}'")

some_decorator(decorated_function("python"))
some_decorator(myfunction("myfunc"))

#some_decorator, "try"