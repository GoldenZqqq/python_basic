class Player(object):  # object 基类
    def __init__(self, name, age, city):  # 初始化函数
        self.name = name
        self.age = age
        self.city = city


mia = Player("mia", 24, "上海")
print(mia.name, mia.age, mia.city)
tom = Player("tom", 34, "北京")
tom.height = 180
tom.age = 32
print(tom.__dict__)  # 获取实例(对象)的所有属性


# 武器：名字 攻击值 等级
class weapon(object):
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        pass


gun = weapon("AK47", 1000, 3)
print(gun.__dict__)
