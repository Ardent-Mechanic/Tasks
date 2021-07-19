import string
import random


def task1():
    sumbols = "KOROVA"
    with open("easy1.txt", mode="w", encoding="utf8") as data:
        for _ in range(1000):
            st = ""
            for _ in range(random.randint(500, 800)):
                st = st + random.choice(sumbols)
            data.write(st + "\n")


def task2():
    sumbols = string.ascii_uppercase
    with open("easy2.txt", mode="w", encoding="utf8") as data:
        st = ""
        for _ in range(1000000):
            st = st + random.choice(sumbols)
        data.write(st)


def task3():
    sumbols = "!@#№$;%^:&?*()-_=+{}[]<>,." + string.ascii_letters + string.digits
    with open("normal1.txt", mode="w", encoding="utf8") as data:
        for _ in range(1000):
            st = ""
            for _ in range(random.randint(500, 800)):
                st = st + random.choice(sumbols)
            data.write(st + "\n")


def task4():
    sumbols = string.ascii_letters
    with open("normal2.txt", mode="w", encoding="utf8") as data:
        for _ in range(1000):
            st = ""
            for _ in range(random.randint(500, 800)):
                st = st + random.choice(sumbols)
            data.write(st + "\n")


def task5():
    sumbols = "<==========================>"
    with open("hard1.txt", mode="w", encoding="utf8") as data:
        for _ in range(1000):
            st = ""
            for _ in range(random.randint(500, 800)):
                st = st + random.choice(sumbols)
            data.write(st + "\n")


def task6():
    sumbols = string.ascii_uppercase + string.digits
    with open("hard2.txt", mode="w", encoding="utf8") as data:
        for _ in range(1000):
            st = ""
            for _ in range(random.randint(500, 800)):
                st = st + random.choice(sumbols)
            data.write(st + "\n")


def task7():
    vowels = list("aeiou")
    consonant = list("bcdfghjklmnpqrstvwxyz")
    web_site_names = []
    for _ in range(10):
        name = ""
        for i in range(random.randint(7, 12)):
            if i % 2 == 0:
                name = name + random.choice(consonant)
            else:
                name = name + random.choice(vowels)
        name = name[:-3] + "." + name[-3:]
        web_site_names.append(name)
    with open("unusual.txt", mode="w", encoding="utf8") as data:
        for site_name in web_site_names:
            data.write(site_name + "\n")
            for _ in range(100):
                ip = str(random.randint(0, 300)) + "." + str(random.randint(0, 300)) + "." + str(
                    random.randint(0, 300)) + "." + str(random.randint(0, 300)) + ":" + str(random.randint(80, 3128))
                data.write(ip + "\n")


if __name__ == '__main__':
    """Функции для генерации новых файлов для заданий"""
    pass
    # task1()
    # task2()
    # task3()
    # task4()Л
    # task5()
    # task6()
    # task7()
