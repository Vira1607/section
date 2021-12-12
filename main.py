print('Отрезок')

# Программа считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b],
# которые кратны числу 3.

number_first = int(input('Начало отрезка: '))
number_twice = int(input('Конец отрезка: '))

counter = 0
summary = 0

for i in range(number_first, number_twice + 1):
    if i % 3 == 0:
        counter += 1
        summary += i

print(summary / counter)
