## OOP , Polymorphism

class Batch:
    def course(self):
        print("Generic course")

class PythonBatch(Batch):
    def course(self):
        print("Python Course")

class JavaBatch(Batch):
    def courses(self):
        print("Java course")


def show_course(obj):
    obj.course()

# show_course(PythonBatch())
# show_course(JavaBatch())

# o1 = PythonBatch()
# o2 = JavaBatch()

# o1.course()
# o2.course()


### 1 duck typing, 2 inheritance

class PythonBatch():
    def course(self):
        print("Python Course")

class JavaBatch():
    def course(self):
        print("Java course")

def show_course(obj):
    obj.course()

# show_course(PythonBatch())
# show_course(JavaBatch())



### abstracton
from abc import ABC, abstractmethod

## this is my base class or my blue print for abstraction implementions
class Batch(ABC):
    @abstractmethod
    def syllabus(self):
        pass

class PythonBatch(Batch):
    def syllabus(self):
        print("python, AI, ML")

class JavaBatch(Batch):
    def syllabus(self):
        print("Java, Javaconpts")

# # working cases
# p = PythonBatch()
# j = JavaBatch()

# p.syllabus()
# j.syllabus()

# not working
class DotNetBatch(Batch):
    def duraiton():
        print("thie is durations")

# d = DotNetBatch()


#### Encapsulation

# no encapsulation and changing the data

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# s = Student("ravi", 100)


# #manupulate or change

# s.marks = -1
# print(s.marks, "changed value")

### Encapsulation, writing Private variables

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   ## prevent this from being changes, make it private

    def get_marks(self):
        return self.__marks
    
    def __private(self):
        print("dome some private method work")
    
s = Student("ravi", 200)
print(s.get_marks())

s.__marks = 1212
print(s.__marks)

##print(s.name)


class Batch:
    def start(self):
        print("Database connection made succefully!")


class PythonBatch(Batch):
    def start(self, a,b):
        super().start()
        print("Processing Started")

p = PythonBatch()
p.start()

### database connection, data processing 

### decorator , generate, classmethod, staticmethod, method overridering and overloading