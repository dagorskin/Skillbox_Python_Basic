import random  # Для большего интереса подключаем пвсевдо-рандом.
print('Задача 6. Успеваемость в классе')
print('---' * 15)  # Разделитель.

students = int(input('Введите количество учеников: '))
scores, threes, fours, fives = [], 0, 0, 0
for count in range(0, students):  # Заполняем список оценок случайными числами.
    score = random.randint(3, 5)
    scores.append(score)
for score in scores:  # Подсчет количество тех или иных оценок.
    if score == 3:
        threes += 1 
    elif score == 4:
        fours += 1
    else:
        fives += 1
# Вывод результата.
if threes >= fours and threes >= fives:
    print('Из ', students, ' учеников больше всего троечников (', threes, ').', sep='')
elif fours >= threes and fours >= fives:
    print('Из ', students, ' учеников больше всего хорошистов (', fours, ').', sep='')
elif fives >= threes and fives >= fours:
    print('Из ', students, ' учеников больше всего отличников (', fives, ').', sep='')
else:
    print('Всех поровну')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.