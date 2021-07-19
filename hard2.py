"""Текстовый файл соcтоит не более чем из 1000 строк, которые состоят латинских букв в верхнем регистре и десятичных цифр.
Найдите минимальный номер строки с палиндромом максимальной длинны и выведите сам палиндром, через пробел.
 Палиндром это строка, которая одинаково читается как слева направо, так и справа на лево. 123ASA321 - палиндром.
 Нумерация строк начинается с единицы.

Пример. Исходный файл:
1. ASD1554GD1SY
2. HA545K2J2K5J4
3. J1J59VM9J29FJ
4. 94JF1KOROK12

В этом примере в строке 2 встречается строка-палиндром: 5K2J2K5, а в строке 4: 1KOROK1.
Ответ: 2 5K2J2K5
"""


def palindrome_cheker(string):
    palindrome_len = 0
    pal = ""
    s = string
    for start in range(len(s)):
        copy_string = s[start:]
        for _ in range(s.count(s[start]) ** 2):
            end = copy_string.rfind(s[start])
            if copy_string[:end + 1] == copy_string[:end + 1][::-1]:
                if palindrome_len < len(copy_string[:end + 1]):
                    palindrome_len = len(copy_string[:end + 1])
                    pal = copy_string[:end + 1]
                break
            if end - 1 > start:
                copy_string = copy_string[:end]
            else:
                break
    return palindrome_len, pal


with open("hard2.txt") as f:
    data = f.readlines()
    max_len = max_len_in_string = 0
    min_index = 1001
    max_palindrome = palindrome = "-"
    for index in range(len(data)):
        string = data[index].strip()
        max_len_in_string, palindrome = palindrome_cheker(string)

        if max_len_in_string > max_len or (max_len == max_len_in_string and min_index > index):
            min_index = index
            max_palindrome = palindrome
            max_len = max_len_in_string
print(min_index + 1, max_palindrome)
