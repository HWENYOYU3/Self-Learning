# set = set()
# print(set)

# add()
# mySet = set()
# mySet.add(20)
# print(mySet)

# discard()
# mySet = set({20, 30, 40})
# mySet.discard(30)
# print(mySet)  #{40, 20}

# union(), intersection() and difference()
# a = {1, 3, 4, 5, 7}
# b = {3, 4, 8, 9, 10}
# print(a.difference(b))  #{1, 5, 7}
# print(b.difference(a))  #{8, 9, 10}
# print(a.intersection(b))  #{3, 4}
# print(b.intersection(a))  #{3, 4}
# print(a.union(b))  #{1, 3, 4, 5, 7, 8, 9, 10}
# print(b.union(a))  #{1, 3, 4, 5, 7, 8, 9, 10}

# issubset(), issuperset()
# a = {1, 3, 4, 5, 7}
# b = {1, 3, 4, 5, 7, 8, 9, 10}
# print(a.issubset(b))  # True
# print(a.issuperset(b))  # False
# print(b.issubset(a))  # False
# print(b.issuperset(a))  # True
