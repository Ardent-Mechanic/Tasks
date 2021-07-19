"""Текстовый файл соcтоит не более чем из 1000000 латинских букв в верхнем регистре.
Требуется найти букву, которая чаще всех встречается в файле и вывести ее вместе с количетсвом повторений.
Если максимальное количетсво имеют несколько букв, вывести ту, что стоит первее по алфавиту.

Пример. Исходный файл:
AAAAADDFFFXXXXBBBBNNNNN

Ответ: 5A
"""

with open("easy2.txt") as f:
    data = f.read()
    sl = dict()
    for letter in data:
        if sl.get(letter, False):
            sl[letter] += 1
        else:
            sl[letter] = 1

k = max(sorted(sl.keys()), key=lambda key: sl[key])
print(sl[k], k, sep="")


