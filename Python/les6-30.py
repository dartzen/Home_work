# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент: "))
n = int(input("Введите разность элементов: "))
d = int(input("Введите кол-во элементов: "))


an = a + (n - 1) * d
arr = []
for i in range(a, an+1, d):
    arr.append(i)
print(arr)