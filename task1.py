'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''

number = int(input('Введите трехзначное число: '))

num1 = int(number / 100)
num2 = int(number % 100 / 10)
num3 = int(number % 10)
result = num1 + num2 + num3
print (result)