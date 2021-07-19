"""Текстовый файл соcтоит не более чем из 1000 строк, которые состоят латинских букв. Обратите внимание, что регистр
 у букв может быть любым. Определите количество строк в которых встречается комбинация  B**R, так как мы рассматриваем
 буквы во всех регистрах, нужно учесть такие комбинации как B**r, b**R, b**r. Всего получается 4 комбинации: B**R, B**r, b**R, b**r.

Пример. Исходный файл:
1. asBiorUio
2. hBkWdfAW
3. basRFgAsd
4. HiRjaDitg

В этом примере в строке 1 встречается комбинация Bior - B**r, а в строке 3 basR - b**R.
Ответ: 2
"""

with open("normal2.txt") as f:
    data = f.readlines()
    max_count = 0
    for index in range(len(data)):
        string = data[index].upper().strip()
        while "B" in string:
            start = string.find("B")
            if start + 3 >= len(string):
                break
            if string[start + 3] == "R":
                max_count += 1
                break
            string = string[start + 1:]

print(max_count)
