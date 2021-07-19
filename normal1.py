"""Текстовый файл содержит строки различной длины. Строки содержат всевозможные символы, буквы в нижнем регистре присутствуют.
Определите максимальный номер строки, в которой максимально количество подряд идущих символов, состоят только из букв и цифр.
Нумерация строк начинается с единицы.

Пример. Исходный файл:
1. !AsD5414^32&
2. 15H!jo(0)1
3. Ni**1d1y_1+
4. (12Jack0+12Fg12)

В этом примере в строке 1 семь символов, удовлетворяющих условию - (AsD5414), также в строке 4 семь символов - 12Jack0.
Ответ: 4
"""

with open("normal1.txt") as f:
    bg_start, bg_end = ord("A"), ord("Z")
    num_start, num_end = ord("0"), ord("9")
    data = f.readlines()
    max_count = max_index = 0
    for index in range(len(data)):
        count = 0
        for sumbol in data[index].upper().strip():
            n = ord(sumbol)
            if bg_end >= n >= bg_start or num_end >= n >= num_start:
                count += 1
            else:
                if max_count <= count:
                    max_count = count
                    max_index = index
                count = 0
print(max_index + 1)
