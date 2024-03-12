# built-in hash function, hash(hashable object)

# a = 100
# b = 2.0
# c = "hello"
# d = False
# e = (10, "why")
# print(hash(a), hash(b), hash(c), hash(d), hash(e))
# 100 2 5672211561375050706 0 -2835569262471823306


# __hash__() function
# class Robot:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     # define a private method __key()
#     def __key(self):
#         return (self.name, self.age, self.address)

#     # implement __hash__() function
#     def __hash__(self):
#         return hash(self.__key())


# robot_1 = Robot("Kevin", 25, "Taiwan")
# dictionary = {robot_1: "Kevin"}
# print(dictionary[robot_1])


# --------------------------
# __eq__() function
class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented


robot_1 = Robot("Kevin", 25, "Taiwan")
robot_2 = Robot("Kevin", 25, "Taiwan")
print(robot_1 == robot_2)
