"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
print_operation_table(lambda x, y: x * y)
"""

def print_operation_table(operation, num_rows=5, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(*list(map(operation, [i], [j])), end="\t")
        print()

num_rows = int(input("Введите количество строк: "))
num_columns = int(input("Введите количество колонок: "))

print_operation_table(lambda x, y: x * y, num_rows, num_columns)



