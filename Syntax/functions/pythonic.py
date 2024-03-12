# 打包與開箱 packing, unpacking to achieve variable changes
# a = 10
# b = 5
# a, b = b, a
# print(f"a 的值是 {a} , b 的值是 {b}")  # a 的值是 5 , b 的值是 10


# comparison operator in Python
# b = 30
# if 10 < b < 50:
#     print("b is in (10,50)")

# membership operator in if statement
myString = input("please enter the day you want to go (Mon, Tue, ..., Sun)...")
if myString in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"):
    print(f"{myString} is the day you want to go?")
else:
    print("invalid input")
