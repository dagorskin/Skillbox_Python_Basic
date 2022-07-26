print('Задача 5. Факториал')
print('---' * 15)  # Разделитель.

sum_n = 1
number_n = int(input('Введите число что бы найти его факториал: '))
for number in range(1, number_n):
    sum_n += sum_n * number
print('Факториал числа ', number_n, ' равен ', sum_n, '.', sep='')

# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
# 
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
# 
# Запись N! означает следующее:
# 
# N! = 1 * 2 * 3 * 4 * 5 * … * N
# 
# Пример:
# 
# Введите число: 5
# Факториал числа 5 равен 120
