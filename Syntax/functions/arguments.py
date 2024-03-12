# positional arguments vs keyword argument
# def exponent(a, b):
#     return a**b


# keyword arguments
# print(exponent(a=2, b=3))  # 8
# print(exponent(b=3, a=2))  # 8


# default arguments
# def addition(n1, n2=1):
#     return n1 + n2


# print(addition(5))  # 6


# *args
# def sum(*args):
#     print(args)
#     print(type(args))


# sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# <class 'tuple'>


## *kwargs
# def myFunc(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# myFunc(name="Kevin", age=25, address="Taiwan")
# {'name': 'Kevin', 'age': 25, 'address': 'Taiwan'}
# <class 'dict'>


# def myFunc(*args, **kwargs):
#     print("I would like to eat {} {}".format((args[1]), kwargs["food"]))


# myFunc(10, 20, 30, food="eggs", price=15, address="US")
#  I would like to eat 20 eggs


# all arguments in one function
def myFunc(n1, n2, n3=4, *args, **kwargs):
    print(n1, n2, n3, args, kwargs)


myFunc(1, 2, 3, 4, 5, x=2, y=3)
# 1 2 3 (4, 5) {'x': 2, 'y': 3}
