print('Задача 8. Замечательные числа')
print('---' * 15)  # Разделитель.

number_list = []
for number in range(10, 100):
    if number == ((number // 10) * (number % 10)) * 3:
        number_list.append(number)
print('Те самые двузначные числа:', str(number_list)[1:-1])

# Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.