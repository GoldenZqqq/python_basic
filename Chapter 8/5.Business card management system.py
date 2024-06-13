cards = [
    {
        "name": "jack",
        "phone": "1381111111",
        "qq": "123456789",
        "email": "123456789@qq.com",
    },
    {
        "name": "tom",
        "phone": "1382222222",
        "qq": "987654321",
        "email": "987654321@qq.com",
    },
    {
        "name": "lucy",
        "phone": "1383333333",
        "qq": "111111111",
        "email": "111111111@qq.com",
    },
]


def menu():
    print("*" * 30)
    print(
        """欢迎使用【名片管理系统】
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统"""
    )
    print("*" * 30)


def new_card(name, phone, qq, email):
    user = {"name": name, "phone": phone, "qq": qq, "email": email}
    cards.append(user)
    return True


def show_card():
    for card in cards:
        print("*" * 30)
        print(
            """姓名：%s
电话：%s
QQ：%s
邮箱：%s"""
            % (card["name"], card["phone"], card["qq"], card["email"])
        )
        print("*" * 30)


def query_card():
    for card in cards:
        for k, v in card.items():
            if kw == v:
                return card


def quit():
    print("欢迎下次使用")


menu()
while True:
    op = input("请输入你要操作的序号：")
    if op == "1":
        name = input("请输入你的姓名：")
        phone = input("请输入你的电话号码：")
        qq = input("请输入你的QQ号码：")
        email = input("请输入你的邮箱地址：")
        result = new_card(name, phone, qq, email)
        if result:
            print("名片添加成功！")
        else:
            print("名片添加失败，请重试！")

    elif op == "2":
        show_card()
    elif op == "3":
        kw = input("请输入查询的关键字：")
        result = query_card(kw)
    elif op == "0":
        quit()
        break
    else:
        print("请重试")
