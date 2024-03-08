# tic toc toe game

row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]

counter = 0


# 建立九宮格
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


# 使用者輸入的值
def user_choice():
    choice = input("please enter a number between 1 and 9 ... ")
    # 如果輸入的東西不是數字, 或是數字不介於 0-9 之間, 則要求重新輸入
    while not choice.isdigit() or int(choice) not in range(1, 10):
        if not choice.isdigit():
            print("ur enter is not valid !")
        elif int(choice) not in range(1, 10):
            print("ur enter is not between 1 and 9 !")
        choice = input("please enter a number between 1 and 9 ... ")
    # return 輸入的數字
    return int(choice)


# 該顯示 'O' 還是 'X'
def get_symbol():
    global counter
    symbol_list = ["X", "O"]
    counter += 1
    print(counter)
    # 在執行第一次時, 填入 'O'
    return symbol_list[counter % 2]


# 根據填入的數字, 來更新九宮格
def update_display(number):

    global row1, row2, row3
    # index 當作使用者輸入的值, 如果輸入的值介於 1-3 之間, 則 row 1 對應的 index 值是 0-2, 發生更改
    # 先檢查要更改的位置是不是 "", 是的話就更改值, 並 return True
    if number in range(1, 4):
        if row1[number - 1] == "":
            row1[number - 1] = get_symbol()
            return True
        else:
            return False
        # 輸入的值介於 4-6, 將他們轉換成 row 對應的 index 值 0-2
    elif number in range(4, 7):
        if row2[number % 3 - 1] == "":
            row2[number % 3 - 1] = get_symbol()
            return True
        else:
            return False
    elif number in range(7, 10):
        if row3[number % 3 - 1] == "":
            row3[number % 3 - 1] = get_symbol()
            return True
        else:
            return False

    print(row1)
    print(row2)
    print(row3)


# 判斷是否獲勝
# row1 = ["", "", ""]
# row2 = ["", "", ""]
# row3 = ["", "", ""]
def winner_checking():
    # 預設沒有贏家, 等到下列程式碼確認完後, 在賦予 ply1, ply2 真值
    player1 = False
    player2 = False
    # 獲勝條件一
    if row1[0] == row1[1] and row1[1] == row1[2] and "" not in row1:
        if row1[0] == "X":
            player2 = True
        elif row1[0] == "O":
            player1 = True
    # 獲勝條件二
    elif row2[0] == row2[1] and row2[1] == row2[2] and "" not in row2:
        if row2[0] == "X":
            player2 = True
        elif row2[0] == "O":
            player1 = True
    # 獲勝條件三
    elif row3[0] == row3[1] and row3[1] == row3[2] and "" not in row3:
        if row3[0] == "X":
            player2 = True
        elif row3[0] == "O":
            player1 = True
    # 獲勝條件四
    elif (
        row1[0] == row2[0]
        and row2[0] == row3[0]
        and (row1[0] != "" and row2[0] != "" and row3[0] != "")
    ):
        if row1[0] == "X":
            player2 = True
        elif row1[0] == "O":
            player1 = True
    # 獲勝條件五
    elif (
        row1[1] == row2[1]
        and row2[1] == row3[1]
        and (row1[1] != "" and row2[1] != "" and row3[1] != "")
    ):
        if row1[1] == "X":
            player2 = True
        elif row1[1] == "O":
            player1 = True
    # 獲勝條件六
    elif (
        row1[2] == row2[2]
        and row2[2] == row3[2]
        and (row1[2] != "" and row2[2] != "" and row3[2] != "")
    ):
        if row1[2] == "X":
            player2 = True
        elif row1[2] == "O":
            player1 = True
    # 獲勝條件七
    elif (
        row1[0] == row2[1]
        and row2[1] == row3[2]
        and (row1[0] != "" and row2[1] != "" and row3[2] != "")
    ):
        if row1[0] == "X":
            player2 = True
        elif row1[0] == "O":
            player1 = True
    # 獲勝條件八
    elif (
        row1[2] == row2[1]
        and row2[1] == row3[0]
        and (row1[2] != "" and row2[1] != "" and row3[0] != "")
    ):
        if row1[2] == "X":
            player2 = True
        elif row1[2] == "O":
            player1 = True

    if player1:
        return "player 1 wins !"
    elif player2:
        return "player 2 wins !"
    else:
        return "no one wins !"


# 主遊戲程式
def start_game():
    # 先畫出九宮格
    display(row1, row2, row3)
    # 使用者輸入數字, 並更新表格
    while True:

        while True:

            if update_display(user_choice()):
                break
            else:
                print("wrong position to ur choice !")

        # 判斷是否有玩家獲勝
        result = winner_checking()
        if result == "player 1 wins !":
            display(row1, row2, row3)
            print("player 1 is winner !")
            return
        elif result == "player 2 wins !":
            display(row1, row2, row3)
            print("player 2 is winner !")
            return
        elif result == "no one wins !" and counter == 9:
            print("the game is tie, no one wins the game !")
            return
        # 在判斷完還沒有玩家獲勝時, 印出現在的結果
        display(row1, row2, row3)


start_game()
