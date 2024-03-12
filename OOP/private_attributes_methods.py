# private attributes and methods can only use in the class that define those characteristics
# use __ before attributes / methods definition


# Private Attributes
# class Robot:
#     def __init__(self, name):
#         self.__name = name

#     def walking(self):
#         print(f"{self.__name} is walking ...")


# robot_1 = Robot("Kevin")
# robot_1.walking()
# Kevin is walking ...
# robot_1.__name
# 無法從外部訪問 private attribute
# AttributeError: 'Robot' object has no attribute '__name'

# -----------------------


# Private Methods
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __introduction(self):
#         print(f"Hello, my name is {self.name}, {self.age} years old.")

#     def walking(self):
#         self.__introduction()
#         print("I'm from Taiwan.")


# people_1 = People("Kevin", 25)
# people_1.walking()
# Hello, my name is Kevin, 25 years old
# I'm from Taiwan


# Encapsulation


class Robot:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def age_setter(self, new_age):
        if new_age > 0 and new_age < 100:
            self.age = new_age
        else:
            print("New age setting is invald.")

    def age_getter(self):
        print(self.age)


my_robot = Robot("Kevin", 25)
my_robot.age_setter(50)
my_robot.age_getter()
