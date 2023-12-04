# Задание 2
# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

import sys

# Импорт нужен, чтобы увеличить установленный в последних версиях питона лимит(4300)
# на вывод максимального кол-ва строк
sys.set_int_max_str_digits(0)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in fibonacci():
    if count == 5:
        print(f"{count}е число Фибоначи = {number}")
    if count == 200:
        print(f"{count}е число Фибоначи = {number}")
    if count == 1000:
        print(f"{count}е число Фибоначи = {number}")
    if count == 100000:
        print(f"{count}е число Фибоначи = {number}")
        break
    count += 1
