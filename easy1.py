"""Текстовый файл содержит строки различной длины. Строки содержат буквы CKRVAO.
Определите минимальный номер строки, в которой слово KOROVA встречается ровно 2 раза.
Нумерация строк начинается с единицы.

Пример. Исходный файл:
1. CARKVOAKRC
2. VAORKVKAR
3. VKOROVAC
4. CAVRKVORA
5. CARKOROVA

В этом примере в строке 3 есть слово KOROVA и в строке 5 есть слово KOROVA, так как мы ищем минимальный номер строки.
Ответ: 3
"""

with open("easy1.txt") as f:
    data = f.readlines()
    for index in range(len(data)):
        string = data[index].strip()
        if string.count("KOROVA") == 2:
            print(index + 1)
            break

