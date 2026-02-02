# ## set 
# name = {44,32232,121,121212,67,67}
# names = {44444,32232,121,121212,67,67}
# print(name)

# name.add(1231231)
# print(name)

# print(name.difference(names))

# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# c = {5,6,7,8,9}

# print(a.difference(b,c))

# name.copy()


# original_set_object = {"apple", "banana","orange"}
# copied_set = original_set_object.copy()

# print(id(original_set_object))
# print(id(copied_set))

# print(original_set_object)
# print(copied_set)
# copied_set.add("cherry")
# print(copied_set, "afterr adding")

# l = [1,2,3,4,5,6,7,8,9,9]
# S = set(l)
# print(S)

## tuple
# tpl = (1,2,3,4,5,6,6,6,6,6,6,6,6)
#        #0,1,2,3,4,5,6,7
# print(tpl)
# print(tpl.count(6))
# print(tpl.index(6))

# color = (11,22,33)
#         # R, G,  b
# Database_connection  = ("databasename","connectonstring")

# classes and objects

### loops, if else conditions

# for 
# while


# if
# else
# elif
# finally








# for_loop_example(1,2,3,4,5,6,76)
# obj = while_loop_example([2,3,4,5,6,7,8,9])
# print(obj)


class Bind_Inside_Class:
    def for_loop_example(self,a,b,c,d,f,e,r):
        my_list = [1,2,3,4,5,6,7]
        for i in my_list:
            if 1 in my_list:
                print("DO SOMETHING HERE")
            else:
                print("notthing")
        return ""

    def while_loop_example(self,my_list):
        while 1 in my_list:
            print(my_list)
            my_list.remove(1)
            #print(my_list)
        S = {1,23,4,5}
        t = (1,2,3,2,3,2,3,2,3,23,2)
        return f'returninig three statement {S}, {t}, {my_list}'


my_list = [1,2,3,4,5,6]
class_object = Bind_Inside_Class()
class_object.while_loop_example(my_list)
# class_object.for_loop_example()
print(id(my_list))

class_object1 = Bind_Inside_Class()
class_object.while_loop_example(my_list)
print(id(class_object1))














