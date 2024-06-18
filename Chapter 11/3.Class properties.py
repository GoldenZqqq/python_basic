class Player(object):  # object 基类
    numbers = 0  # 类属性

    def __init__(self, name, age, city):  # 初始化函数
        # 实例属性
        self.name = name
        self.age = age
        self.city = city
        Player.numbers += 1


mia = Player("mia", 24, "上海")
print(mia.__dict__)
print("欢迎 Counter Strike 2 的第%d个玩家加入" % Player.numbers)
tom = Player("tom", 22, "北京")
print("欢迎 Counter Strike 2 的第%d个玩家加入" % Player.numbers)


class weapon(object):
    numbers = 0
    max_damage = 10000
    levels = ["军规级", "受限级", "保密级", "隐秘级", "罕见"]

    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        weapon.numbers += 1
        if damage > weapon.max_damage:
            raise Exception("武器伤害超过限制，请重试！")
        if level not in weapon.levels:
            raise Exception("武器等级不合法，请重试！")


try:
    gun = weapon("AK47", 10000, "保密级")
    print(weapon.numbers)
    arrow = weapon("arrow", 450, "军规级")
    print(weapon.numbers)
except Exception as e:
    print(e)
