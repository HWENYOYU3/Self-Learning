# flow control - if statement
# if False:
#     print("this is so True")
# else:
#     print("this is False")

# Python 中沒有 switch 語法

# 實際範例
name = input("please enter your name ... ")  # string
deposit = input("please input your cash remaining ... ")  # string
isHungry = input("Are you hungry ? (Y/N) ")  # string

if isHungry == "Y":
    print("you are hungry")
    if int(deposit) >= 30:
        print(f"{name} should go to eat breakfast")
    else:
        print(f"{name} is hungry, but he / she did not have enough money")
elif isHungry == "N":
    print("you are not hungry")
else:
    print("please enter the correct character")
