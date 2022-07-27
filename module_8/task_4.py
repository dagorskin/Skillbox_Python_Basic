print('Задача 4. Отрезок')
print('===' * 15)  # Разделитель.

number_a = int(input('Введите точку а: '))
number_b = int(input('Введите точку b: '))
number_c = int(input('Введите число, которое будет проверкой на кратность: '))
total_number, quantity_number = 0, 0
print('===' * 15)  # Разделитель.

if number_a < number_b:  # Действие при нормальном вводе.
    for number in range(number_a, number_b):
        if number % number_c == 0:
            total_number += number
            quantity_number += 1
    print('Средне арифметическое чисел кратных', number_c, 'между отрезком a и b: ' + str(total_number / quantity_number) + ';')
elif number_a > number_b:  # Если наоборот.
    for number in range(number_b, number_a):
        if number % number_c == 0:
            total_number += number
            quantity_number += 1
    print('Средне арифметическое чисел кратных', number_c, 'между отрезком a и b: ' + str(total_number / quantity_number) + ';')
else:
    print('Ошибка!')
# Напишите программу,
# которая считывает с клавиатуры числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b являются промежутком, а c для проверки кратности).
