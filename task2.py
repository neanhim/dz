# Ссылка на диаграммы:
# https://drive.google.com/file/d/1FIlLK7s0PSTR71hMiqZ3JZDl3KsX_oHk/view?usp=sharing
# Задание 2
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#

num = int(input('Введите натуральное число\n'))
odd = 0
even = 0
while num != 0:
    c = num % 10
    num //= 10
    if c % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Четных = {even}, \nнечетных = {odd}")