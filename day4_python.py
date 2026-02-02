### oop concepts

## class level attributes, and function level attributes


class DotNetClass:
    def __init__(self, name):
        self.name = name
        print("dot net inint method is being called", self.name)

    def methodone():
        pass

class JavaClass(DotNetClass):
    def __init__(self, javaname):
        self.javaname = javaname
        print("java class inint method", self.javaname)

    def inheritance_example(self):
        print(f"accessing dotnet init attributes in java class method {self.javaname}")
    
java = JavaClass("java")
java.inheritance_example()



class PythonBatch2026(DotNetClass):
    def __init__(self, batchname, batchtiming, batchduration):
        self.batchname = batchname
        self.batchtiming = batchtiming
        self.batchduration = batchduration
        
        print("the inint method is being called while creating object")
        var = self.batch_name("javabatch")
        print(var)
        

    def batch_name(self, arg):
        print("check if class method is being called", self.batchname)
        self.batchname = arg
        return f"the batch name is {self.batchname}"

    def batch_timing(self):
        return f"batch timiing is {self.batchtiming}"

    def batch_duration(self):
        return f"duration is {self.batchduration}"

    # def __str__(self):
    #     print("is str method is being called or not")
    #     return "this is str magic method"
    

morningbatch = PythonBatch2026("python", "7AM IST", "45DAYS")
morningbatch.batch_duration()





class PythonBatch2027:
    def __init__(self, batchname, batchtiming, batchduration):
        self.batchname = batchname
        self.batchtiming = batchtiming
        self.batchduration = batchduration
        print("the inint method is being called while creating object")
        self.batch_name()

    def batch_name(self):
        print("check if class method is being called", self.batchname)
        return f"the batch name is {self.batchname}"

    def batch_timing(self):
        return f"batch timiing is {self.batchtiming}"

    def batch_duration(self):
        return f"duration is {self.batchduration}"

    def __str__(self):
        return "this is str magic method"

class PythonBatch2028:
    def __init__(self, batchname, batchtiming, batchduration):
        self.batchname = batchname
        self.batchtiming = batchtiming
        self.batchduration = batchduration
        print("the inint method is being called while creating object")
        self.batch_name()

    def batch_name(self):
        print("check if class method is being called", self.batchname)
        return f"the batch name is {self.batchname}"

    def batch_timing(self):
        return f"batch timiing is {self.batchtiming}"

    def batch_duration(self):
        return f"duration is {self.batchduration}"

    def __str__(self):
        return "this is str magic method"
