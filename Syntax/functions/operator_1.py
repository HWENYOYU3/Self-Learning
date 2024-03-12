# logical operator

# a = True
# b = False
# print(a and b)  # False
# print(not a)  # False
# print(a or b)  # True


# bitwise operator

# a = 60
# b = 13
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)  # 所有 bits 做 not
# print(a << 2)  # 所有 bits 往左移 2
# print(a >> 2)  # 所有 bits 往右移 2


# Truthy, Falsy
# if []:
#     print("hello world!")
# else:
#     print("hello python")  # [] is falsy

# bool()
# print(bool([]))  # False


# short-circuiting evaluation
if 2 or (10 / 0):
    print("we got no error")  # we got no error
