# tps = (10, "hello", True, 10, 20)
# print(len(tps))  #3
# print(tps[0])    #10
# print(tps[0:2])  #(10, 'hello')
# print(tps.count(10))  #2
# print(tps.index(True))  #2


# tuple packing
# x = 10, 15
# print(x)  #(10, 15)
# print(type(x))  #<class 'tuple'>

# tuple unpacking
# a, b = (15, 20)
# print(f"a 的值為 {a} , b 的值為 {b} ") #a 的值為15, b 的值為20

#tuple packing and tuple unpacking
# x = 15
# y = 20
# x, y = y, x
# print(f"x 的值為 {x}, y 的值為 {y}")

# if an element in typle is mutable, then we can choose the element to change it
tps = ([1, 2, 3], "hello")
tps[0][1] = 50
print(tps)  #([1, 50, 3], 'hello')
