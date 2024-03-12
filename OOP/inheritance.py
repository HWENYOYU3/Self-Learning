# 繼承（inheritance）, 將一個 class 內的 attributes 和 methods 繼承自其他的 class
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sleep(self):
#         print(f"{self.name} is sleeping ... ")


# class Student(People):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id


# student_1 = Student("Kevin", 25, 100)
# print(student_1.name, student_1.age, student_1.student_id)
# student_1.sleep()


# ----------------------------------
# Multiple Inheritance
class C:
    def do_stuff(self):
        print("hello from class C")


class D:
    def do_another_stuff(self):
        print("hello from class D")


class A(C, D):
    pass


a = A()
a.do_stuff()
a.do_another_stuff()
