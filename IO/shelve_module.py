import shelve


# use shelve to serialization
# integer1 = [1, 2, 3, 4, 5, 6]
# integer2 = [7, 8, 9, 10, 11, 12]
# integer3 = [100, 101, 102, 103]

# with shelve.open("my_shelf_file", "c") as shelf:
#     shelf["int1"] = integer1
#     shelf["int2"] = integer2
#     shelf["int3"] = integer3


with shelve.open("my_shelf_file", "r") as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf["int1"])
