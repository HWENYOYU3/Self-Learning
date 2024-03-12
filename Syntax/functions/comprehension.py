# list comprehension
# myList = [1, 2, 3, 4]
# newList = [items**2 for items in myList if items >= 2]
# print(newList)  # [4, 9, 16]


# dictionary comprehension
# myList = [1, 2, 3, 4]
# newDict = {items: items**2 for items in myList if items >= 2}
# print(newDict)  # {2: 4, 3: 9, 4: 16}

# set comprehension
# myList = [1, 2, 3, 4]
# newSet = {items**2 for items in myList if items >= 2}
# print(newSet)  # {16, 9, 4}

# generator comprehension
x = [1, 2, 3, 4]
x_squared_generator = (items**2 for items in x)
print(x_squared_generator)  # <generator object <genexpr> at 0x10069f510>
for i in x_squared_generator:
    print(i)
# 1
# 4
# 9
# 16
