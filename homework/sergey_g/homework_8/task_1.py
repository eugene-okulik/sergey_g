# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, 
# bonus - bool. Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random
from random import choice
from random import randint

salary = int(input("Введите число: "))
bonus = random.choice([True, False])
value = f'{salary}, {bonus}'
if bonus:
    salary += random.randint(100, 1000)
print(f" {value} - '${salary}'")
