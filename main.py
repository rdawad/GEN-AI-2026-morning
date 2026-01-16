### what are the data strcuture and data types in python 
# integer > 1,2,3,4
# string > "string", 'string and mae'
# 4.333, 445545.44 floting point 
# True , Flase > boolean
# 2i + 3j > complex data type 

# data structure
# import collections

# collections.defaultdict()

# List .> arrays

name = ["ravi", "kiran", 1,2,3,4,4,5,6, True, False, 3333.5, 5656565.5] # list 
name_array = ["ravi", "kiran", "sam"] ## array 
integer_array = [1,2,3,4,5,6,7,8,9,0,3,4,4,4,4,4] # array
len(integer_array)
#index =          0,1,2,3,4,5,6,7,8,9,10,11,12
print(name, "printg list")
# it can contain duplicates
# its mutable 
# its in order

dictionary_data  = {"name": 222.3, 
                    23232.2: 23232.2, 
                    "keys": "values",
                    True:False,
                    "name":"False",
                    "name": [1,2,3,4,5,6,76]
                    }
print(dictionary_data, "printgin dictionary")
another_dict = {"name": ["ravi","sam",2,3,4,4,5,6, "6", 6]}
print(another_dict)
d = {"name": {"name": "ravi"}} # valied
### D = {["name"]: "value"} # invalid dictionary

### key value, cannot contain, data type except any data structure, ordered, mutable

#tuple(), and , set{}, list[], dict{}

Set_datastructure = {1,2,3,4,5,6,7,8,9,"data",7}
print(Set_datastructure) # mutable, unordered, not a key value , doest not contain duplicate


tuple_data = (0,1,2,3,4,5,5,5,1,6,5,4,5,7, (1,2,3), ({"name":"value"}))
print(tuple_data, "print tuple data") ## immutable, can contain duplicate, ordered

### scripting vs OOP

# oop , inheritance, polymorphism, encapsu;ation, abstraction

from day4_python import PythonBatch2026, PythonBatch2027, PythonBatch2028

