## class method static method, method overloading and method overriding

## class method decorator which only works on class not on object , PEP 8


class Batch:
    center = "Tech Hub"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_center(cls, new_name):
        cls.center = new_name


# b = Batch("Python")
# print(b.center)

# Batch.change_center("New Hub")

# print(b.center)

## static method

class Batch:
    
    def info():
        print("some training info")
        return 'info method'

# batch = Batch.info()
# print(batch)


class Calc:
    def __init__(self,c):
        self.c = c
        print("initialized" , self.c)

    @staticmethod
    def add(a, b):
        return a + b 
    
    def divide( x,y):
        re = x /y
        
        print(re)

# ress = Calc("c value")
# reee = ress.add(3,3)
# print(reee)
# print(type(reee))

var1 = Calc.add(4,5)
var2 = Calc.divide(5,2)

# print(var1, type(var1))
# print(var2, type(var2))

# print(id(var2))
# print(id(var1))



# d = Calc.add(5,6)
# print(d)

# another_var = Calc.divide(6,2)
# print(another_var)

# res = Calc.add(2,4)
# print(res)
# print(type(res))

### method overloading