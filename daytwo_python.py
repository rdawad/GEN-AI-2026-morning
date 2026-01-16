# names = ["RAVI","SAM","JAY"]

# # print(names, "before appending")
# # names.append("james")

# # print(names, "after appending")

# # names.count("RAVI")
# # print(names.count("RAVI"))

# # names.reverse()
# # print(names)

# # names.insert(2, "june")
# # print(names)

# # print(id(names), "before")
# # names.reverse()
# # print(id(names), "after")
# # print(names, "before")
# # print(id(names))

# # names.reverse()

# # print(names, "after")
# # print(id(names))

# names.index("RAVI")
# print(names.index("RAVI")
# )

# numbers = [10,20,30,40,50,60,70]
# index1 = numbers.index(40)
# print(index1,"index of 40")

# index2 = numbers.index(40, 3)
# print(index2, "index by giving the value")

# #index3 = numbers.index(40, 2,7)
# #print(index3, "if available between 4 to 7th index")
# try:
#     numbers.index(40, 4,7)
#     print("if available between 4 to 7th index")
# except Exception as e:
#     print("given number not available at specific location")


# num = [100,200,4000,500,50000]
# print(id(numbers))
# numbers.extend(num)
# print(numbers, 'this one')
# # print(numbers)
# # print(numbers)
# new_var = num + numbers

# print(numbers)
# print(new_var)
# print(id(new_var))

##dictionaries

D = {"name": [1,2,3,4,5,6,7,8],
    "address":"1231 some address",
    "phonenumber": 9123445454}
get_key = D.keys()
print(get_key)

print(type(get_key))
print(type(D))
convereted_list =  list(get_key)
print(convereted_list, "converted list")
print(type(convereted_list))