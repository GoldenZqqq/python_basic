import random


def rock_paper_scissors():  # 石头剪刀布
    player_score, computer_score = 0, 0
    for i in range(3):
        player = input("请输入你的选择（石头、剪刀、布）：")
        computer = random.choice(["石头", "剪刀", "布"])
        if player == computer:
            player_score += 1
            computer_score += 1
        elif (
            (player == "石头" and computer == "剪刀")
            or (player == "剪刀" and computer == "布")
            or (player == "布" and computer == "石头")
        ):
            player_score += 1
        else:
            computer_score += 1
        print(f"玩家选择：{player}，电脑选择：{computer}")
        print(f"玩家得分：{player_score}，电脑得分：{computer_score}")
    if player_score > computer_score:
        print("恭喜你，你赢了！")
    elif player_score < computer_score:
        print("很遗憾，你输了！")
    else:
        print("平局！")


def guess_number(start=1, end=100):  # 猜数字
    number = random.randint(start, end)
    guess = 0
    while True:
        guess = int(input("请输入你猜的数字："))
        if guess == number:
            print("恭喜你，猜对了！")
            break
        elif guess < number:
            print("猜小了！")
        else:
            print("猜大了！")
