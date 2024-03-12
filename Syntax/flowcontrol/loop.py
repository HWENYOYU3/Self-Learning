# for loop
# for letter in "hello world":
#     print(letter)


# nums = [1, 3, 5, 7, 9]
# for num in nums:
#     print(num**2)

# a list of tuples

# for a, b in [(1, 3), (5, 7), (9, 11)]:
#     print(a + b)

# dictionary (keys)
# Dictionary (keys)
# myDicts = {"name": "Kevin", "age": 25}

# for key, value in myDicts.items():  # .item()的結果為
#     print(f"The key is {key} ; the value is {value} ")


# while loop

# x = 0
# while x < 5:
#     print(x)
#     x += 1


# nested loop
# for i in "1234":
#     for j in "abcde":
#         print(i, j)  # 共執行了 20 次

# pass

# n = 50
# if n == 50:  # 此時不會發生任何事
#     pass
# else:
#     print("n is not 50")


# break
# for i in "123456789":
#     if i == "5":
#         break  # i = 5，終止正在執行的迴圈
#     else:
#         print(i)

# print("after the loop")  # 被執行

# continue
# for i in "abcdefg":
#     if i == "c":
#         continue
#         print("hello")  # 不會被執行
#     print(i)  # 除了 c 以外都被印出


# range() function
# print(range(0, 10, 2))  # range(0, 10, 2)


# enumerate() function
# for item in enumerate("hello"):
#     print(item)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# zip() function
x = [1, 2, 3]
y = ["X", "Y", "Z"]
for tuple in zip(x, y):
    print(tuple)
# (1, 'X')
# (2, 'Y')
# (3, 'Z')
