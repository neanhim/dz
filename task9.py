# Ссылка на диаграммы:
# https://drive.google.com/file/d/1FIlLK7s0PSTR71hMiqZ3JZDl3KsX_oHk/view?usp=sharing
# Задание 9
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
#

def sumnum(n):
    m = n
    sum = 0
    while m != 0:
        sum += m % 10
        m = m // 10
    return sum

num = int(input("Введите натуральное число. 0 - выход\n"))
max = 0
maxsum = 0
while num != 0:
    sum = sumnum(num)
    if sum > maxsum:
        max = num
        maxsum = sum
    num = int(input("Введите натуральное число. 0 - выход\n"))
print(f"Число с максимальной суммой цифр - {max}\n Его сумма цифр - {maxsum}")