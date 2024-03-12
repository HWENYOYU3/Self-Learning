# user_input = input("please enter your age...")
# print("-------------")
# print(user_input)


# 終極密碼遊戲
import random

guess_number = random.randint(0, 100)
print(guess_number)
lower_bound = 0
upper_bound = 100

while True:
    user_guess = int(
        input(f"guess a number between {lower_bound} and {upper_bound} ... ")
    )

    # 無效猜測數字 (猜測的數字小於下邊界與大於上邊界)
    if user_guess < lower_bound or user_guess > upper_bound:
        print("ur guess is invalid, please guess another number")
        continue
    elif user_guess == guess_number:
        print(f"u guess the correct number, it is {guess_number} !")
        break
    elif user_guess > guess_number:
        upper_bound = user_guess
        print(f"the number u guess is too big, please try again !")
        continue
    else:
        lower_bound = user_guess
        print(f"the number u guess is too small, please try again !")
        continue
