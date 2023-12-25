# Задание 1
# Напишите программу: Есть функция которая делает одну из арифметических операций с
# переданными ей числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def operation_decorator(func):
    def wrapper(first, second, operation):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        else:
            if first < 0 or second < 0:
                return func(first, second, '*')

    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

result = calc(first_number, second_number, "")
print("Результат:", result)
