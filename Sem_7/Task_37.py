# Задача №36
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает 
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns 
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с 
# единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой 
# ровно два аргумента, как, например, у операции умножения.

a = int(input("Введите номер строки: "))
b = int(input("Введите номер колонки: "))

def print_operation_table(operation, num_rows=a, num_columns=b):
    for x in range(1, num_rows + 1):
        lists = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            lists.append(num)
        print(*[str(x) for x in lists])

print_operation_table(lambda x, y: x * y)
