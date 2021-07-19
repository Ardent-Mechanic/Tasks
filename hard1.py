"""Текстовый файл содержит строки различной длины. Строки содержат такие символы как: <=>.
Определите максимальное количество подстрок такого вида: ==>.

Пример. Исходный файл:
1. ===>==<==>==><>===<=  Здесь 2 таких подстроки
2. <><>==>==<<<<==> Здесь 2 таких подстроки
3. <==<==<==> Здесь 1 таких подстроки
4. ==>==>=====>>==<==>===> Здесь 3 таких подстроки

В этом примере максимальное количество подстрок ==> равно 3. Такие подстроки как ===>, =======> учитывать не следует
Ответ: 3
"""


def chek_len_string(index, strng):
    num = index
    count = 0
    for i in range(num - 1, -1, -1):
        if strng[i] == "=":
            count += 1
        else:
            break
        if count > 2:
            count = 0
            break
    return count


with open("hard1.txt") as f:
    data = f.readlines()
    max_count = 0

    for index in range(len(data)):
        string = data[index].strip()
        string_count = 0

        while ">" in string:
            n = string.find(">")
            cheker = chek_len_string(n, string)
            if cheker > 0:
                string_count += 1
            string = string[n + 1:]

        max_count = max(max_count, string_count)
print(max_count)
