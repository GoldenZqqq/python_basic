import csv, random
from my_package import my_tools

lista = []


def random_info(n=100):
    subjects = ["python", "java", "C++", "HTML"]
    names = []
    for i in range(n // len(subjects)):
        name = my_tools.random_string(random.randint(3, 6))
        names.append(name)
    for i in range(n):
        name = random.choice(names)
        subject = random.choice(subjects)
        score = random.randint(50, 100)
        for j in lista:
            if j[0] == name and j[1] == subject:
                break
        else:
            lista.append([name, subject, score])


def average():
    with open("Chapter 10/data.csv", "r", encoding="utf-8") as f:
        cf = csv.reader(f)
        head = next(cf)  # 获取表头
        scores = []
        for i in cf:
            scores.append(int(i[2]))
        return sum(scores) / len(scores)


def generate_data():
    with open("Chapter 10/data.csv", "a", encoding="utf-8") as f:
        cf = csv.writer(f, lineterminator="\n")
        random_info()
        cf.writerows(lista)


# generate_data()
result = average()
print("最终获取的平均分：", round(result, 2))
