# Задача №8 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить 
# шоколадку на два прямоугольника).

n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите желаемое колличество долек: '))
if n * m > k and ((k % n == 0) or (k % m == 0)):
    print('Всё получится!')
else:
    print('Не выйдет :(')