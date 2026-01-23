## Decorator


## decorator
def my_decorator(func):
    # this has to do something
    def wrapper():
        print("Executing some processing before fucntion call, some logs")
        func()
        print("some more processing after function call, timestamp")

    #print(wrapper)
    print("before wrapper gets called")
    print("not a location")
    return wrapper

#@my_decorator
def greet():
    print("Hello there")


### generator

#generator function
def number(a,b,c):
    yield a
    print("dome thing")
    yield c
    if type(c) == bool:
        print("define some logic")
    else:
        print("not a bool")

for i in number("ravi", True, True):
    print(i, type(i))
    
 # numpy and pandas