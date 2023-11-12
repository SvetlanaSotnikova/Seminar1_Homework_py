# Task 1
# Найдите сумму цифр трехзначного числа
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

num = int(input("input your number: "))
num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10

res = num1 + num2 + num3

print(f'number = {num} -> result = {res} ({num1} + {num2} + {num3})')

# Task 2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# n = 60 -> 10 40 10 

num = int(input("\ninput the count of cranes: "))
boys = num // 6
girl = 4 * boys

print(f'counr = {num} -> boy 1: {boys}, girl: {girl}, boy 2: {boys}')

# Task 3
# : Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# n = 385916 -> yes
# n = 123456 -> no

num = int(input("\ninput ticket number: "))

num6 = num % 10
num5 = (num // 10) % 10
num4 = (num // 100) % 10
num3 = (num // 1000) % 10
num2 = (num // 10000) % 10
num1 = (num // 100000) % 10

if num1 + num2 + num3 == num4 + num5 + num6:
    print(f"number = {num} -> yes")
else:
    print(f"number = {num} -> no")

# Task 4
# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

a = int(input("\ninput a value for 'a': "))
b = int(input("input a value for 'b': "))
c = int(input("input a value for 'c': "))

if c < a*b and (c % a == 0 or c % b == 0):
    print(f"chocolte size = {a}x{b}, count of slices = {c} -> yes")
else:
    print(f"chocolte size = {a}x{b}, count of slices = {c} -> no") 
