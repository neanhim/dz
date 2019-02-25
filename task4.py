# Ссылка на диаграммы:
# https://drive.google.com/file/d/1FIlLK7s0PSTR71hMiqZ3JZDl3KsX_oHk/view?usp=sharing
# Задание 4
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сколько членов ряда суммировать?\n'))
sum = 0
k = 0
while k <= n - 1:
    sum += 1 / ((-1) ** k * 2 ** k)
    k += 1
print(f"Сумма ряда = {sum}\n")