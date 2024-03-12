# __len__
# __str__
# __repr__
# __add__


class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # define __len__() function, set the return value when we called len()
    def __len__(self):
        return self.age

    # define __str__() function, set the return value when we called str()
    def __str__(self):
        return f"{self.name} is now {self.age} years old ... "

    # define __repr__() function, set the return value when we called repr()
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    # define __add__() function, set the return value when we're doing addition operator
    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented


my_robot = Robot("Kevin", 25)
your_robot = Robot("Tom", 30)
print(len(my_robot))  # 25
print(str(my_robot))  # Kevin is now 25 years old ...
print(repr(my_robot))  # name: Kevin, age: 25
print(my_robot + your_robot)  # 55
