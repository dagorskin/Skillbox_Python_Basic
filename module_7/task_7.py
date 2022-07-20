print('Задача 7. Отрезок')
print('---' * 15)  # Разделитель.

sum_numbers, number_numbers  = 0, 0
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
for number in range(first_num, second_num):  # Цикл с диапазоном от первого до второго числа.
    if number % 3 == 0:  # Отбираем только числа кратные числу 3.
        sum_numbers += number
        number_numbers += 1
arithmetic_mean = sum_numbers / number_numbers
print('Среднее арифметическое чисел от', first_num, 'до', second_num, 'кратных числу три:', arithmetic_mean)

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.