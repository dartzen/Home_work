# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# Вводим количество монеток
# n = int(input("Введите количество монеток: "))

# # Вводим последовательность монеток
# coins = input("Введите последовательность монеток, где '1' - орёл, '0' - решка: ")

# # Создаем переменную для подсчета количества монеток, которые нужно перевернуть
# num_flips = 0

# # Проверяем, какая сторона монеток перекошена больше - "орлы" или "решки"
# if coins.count('1') <= n / 2:
#     target = '0'
# else:
#     target = '1'

# # Переворачиваем монетки, пока не достигнем нужной последовательности
# for i in range(n):
#     if coins[i] != target:
#         num_flips += 1
#         if target == '0':
#             target = '1'
#         else:
#             target = '0'

# # Выводим количество перевернутых монеток
# print("Минимальное количество монет, которые нужно перевернуть:", num_flips)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# # Запрос двух натуральных чисел X и Y (X, Y ≤ 1000)
# X = int(input("Введите натуральное число X (X ≤ 1000): "))
# Y = int(input("Введите натуральное число Y (Y ≤ 1000): "))

# # Вычисляем сумму и произведение этих чисел
# S = X + Y
# P = X * Y

# #Выводим подсказки
# print("Вот сумма и произведение:")
# print(f"Сумма: {S}")
# print(f"Произведение: {P}")

# # Запрос у Кати двух чисел, которые она считает правильными
# guess_X = int(input("Катя, введити число X: "))
# guess_Y = int(input("Катя, введити число Y: "))

# # Проверяем, являются ли введенные Катей числа правильными
# if guess_X == X and guess_Y == Y:
#     print("Верно. Возьми пирожок")
# else:
#     print("Ошибка. Получишь ремня")

# # Дублируем результат Выводим результат
# print(f"Задуманные числа: {X} и {Y}")
# print(f"Сумма: {S}")
# print(f"Произведение: {P}")

#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Запрашиваем у пользователя максимальное значение N
N = int(input("Введите максимальное значение N: "))

# Цикл, выводящий целые степени двойки, не превосходящие N
k = 0
power_of_two = 2**k
while power_of_two <= N:
    print(power_of_two)
    k += 1
    power_of_two = 2**k