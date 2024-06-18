class Player(object):
    numbers = 0  # 类属性
    levels = ["白银", "黄金", "菊花", "老鹰", "地球"]

    def __init__(self, name, age, city, level):  # 初始化函数
        # 实例属性
        self.name = name
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise Exception("段位设置错误！")
        else:
            self.level = level
        Player.numbers += 1

    def show(self):  # 实例方法
        print(
            "我是 Counter Strike 2 的第%d个玩家，我的名字是%s，我来自%s，我的段位是%s"
            % (Player.numbers, self.name, self.city, self.level)
        )

    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1 < len(Player.levels) - 1:
            self.level = Player.levels[index1 + 1]

    def get_weapon(self, weapon):
        self.weapon = weapon

    def show_weapon(self):
        return self.weapon.show_weapon()


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

    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(k, v)


mia = Player("Mia", 24, "上海", "白银")
mia.show()
mia.level_up()
mia.show()
mia.level_up()
mia.show()
mia.level_up()
mia.show()
mia.level_up()
mia.show()
mia.level_up()
mia.show()
mia.level_up()
mia.show()
gun = weapon("AK47", 10000, "隐秘级")
mia.get_weapon(gun)
mia.show_weapon()
