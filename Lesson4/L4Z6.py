# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count
from itertools import cycle

# A
x = input("Введите число, которое будет началом: ")
for i in count(int(x)):
    print(i)

# B
list = [2, 6, 12, 56, 32, 89]
for el in cycle(list):
    print(el)
