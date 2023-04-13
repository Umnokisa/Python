# Задача №26.
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def power(a, b) :
    if b == 1:
        return a
    elif b == 0 :
        return 1
    else:
        return a * power(a, b - 1)
print(power(a, b))