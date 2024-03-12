# # Built-in class in Python

# # my_list = [1, 2, 3, 4]
# # print(type(my_list))

# # <class 'list'>

# ------------------------------------------------------------
# # class
# # 概念等同於 JS 中的 class
# class Robot:
#     # constructor to define attributes in class
#     def __init__(self, name, age):
#         # self.name 為一個 variable
#         self.name = name
#         self.age = age

#     # define method in class
#     def walking(self):
#         print(f"{self.name} is walking ... ")


# my_robot_1 = Robot("Kevin", 25)
# print(my_robot_1.name)
# # Kevin
# print(my_robot_1.age)
# # 25
# my_robot_1.walking()
# # Kevin is walking ...

# ------------------------------------------------------------
# class attribute
# class Robot:

#     ingredient = "metal"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walking(self):
#         print(f"{self.name} is walking ... ")

#     def introduce(self):
#         print(
#             f"Hello, my name is {self.name}, and I'm made of {self.__class__.ingredient}."
#         )


# robot_1 = Robot("Kevin", 25)

# print(robot_1.ingredient)
# print(Robot.ingredient)
# print(robot_1.__class__.ingredient)
# robot_1.introduce()


# ------------------------------------------------------------
# static method
# class Robot:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def sayHello():
#         print("robot says hello !")


# robot_1 = Robot("Kevin", 25)

# robot_1.__class__.sayHello()  # robot says hello !
# ------------------------------------------------------------

# class method, better than static method, cz we don't need to do hard-coding


class Circle:
    """Circle class creates circles"""

    PI = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return (self.radius**2) * self.__class__.PI

    @classmethod
    def total_area(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


c1 = Circle(5)
c2 = Circle(15)
print(c1.area(), c2.area())
print(c1.__class__.total_area())
