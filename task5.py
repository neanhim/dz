# Ссылка на диаграммы:
# https://drive.google.com/file/d/1FIlLK7s0PSTR71hMiqZ3JZDl3KsX_oHk/view?usp=sharing
# Задание 6
#  Вывести на экран коды и символы таблицы ASCII,
#  начиная с символа под номером 32 и заканчивая 127-м включительно.
#  Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

i = 32
while i <= 127:
    for m in range(10):
        print(f"{i} - {chr(i)}", end='\t\t')
        i += 1
        if i > 127:
            break
    print()
