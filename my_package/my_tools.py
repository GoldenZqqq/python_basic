import random
import re


def random_char(upper=True):
    if upper:
        t = random.randint(ord("A"), ord("Z"))
    else:
        t = random.randint(ord("a"), ord("z"))
    return chr(t)


def random_string(length):
    s = ""
    for i in range(length):
        s += random_char(random.choice([True, False]))
    return s


def generate_valid_code(length):
    return random_string(length)


def is_phone_number(phone):
    # 手机号码
    result = re.match(r"^1\d{10}$", phone)
    if result == None:
        return "非法的手机号！"
    return "正确的手机号！"


def is_id_number(ids):
    # 身份证号
    result = re.match(
        r"^\d{6}((20[01]\d)|(202[01234])|(1[89]\d\d))\d{7}[\dX]$", "12345620081234567X"
    )
    if result == None:
        return "非法的身份证号！"
    return "正确的身份证号！"


def main():
    print(generate_valid_code(8))
