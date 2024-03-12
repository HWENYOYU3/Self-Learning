# # index
# print("hello"[1])
# # print("hello"[5]) 超出索引, 印出索引錯誤
# print("hello"[-1])

#slicing
# x = "hello my girl!"
# print(x[0:3])	
# print(x[3:])
# print(x[0:5:2])	
# print(x[::-1])    #倒轉string的常用方法

# print("hello, my name is 'kevin'.")
# print("today is \n a good day")

#concatenation
# myString1 = "hello"
# num1 = 2
# print(myString1 + num1)

#immutable
# myString = "hello"
# myString[0] = "H"
# print(myString)


# built-in function
# name = "Kevin"
# print(name.upper())
# print(name.lower())

# name = "kevin"
# print(name.isupper())				#False
# print(name.islower())				#True

# name = "Kevin"
# print(name.index("v"))			#2

# name = "Kevin"
# print(name.index("s"))			#ValueError: substring not found

# name = "Josh Donaldson"
# print(name.replace("J","KKL"))

# sentence = "today is a good day"
# print(sentence.split(" "))        #['today', 'is', 'a', 'good', 'day']

# sentence = "good day"
# print(list(sentence))               #['g', 'o', 'o', 'd', ' ', 'd', 'a', 'y']

# print("Hello this is {}".format("my resume")) #Hello this is my resume
# print("{}, {}, {}".format(15,"hello",True))   #15, hello, True
# print("{2}, {0}, {1}".format(1, 2, 3))    #3, 1, 2
# print("{name}, {ti}, {address}".format(ti = False, name="kevin", address="Taiwan")) #kevin, False, Taiwan

# name = "kevin"
# print(f"hello, my name is {name}") #hello, my name is kevin

# name = 'kevin'
# print(name.startswith('k')) #True
print("hello" * 2)    #hellohello
