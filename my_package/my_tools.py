import random


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


def main():
    print(generate_valid_code(8))
