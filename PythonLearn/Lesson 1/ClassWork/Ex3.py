# Задание №8
"""
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = int(input('Сколько рядов у ёлки? '))
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (i * 2 + 1))
