# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [543, "sad", 46.345, (1, 3, 71), "rgrg"]
i = 0
print(f"Исходный список: {my_list}")
while ( i < len(my_list)):
    print(f"Тип элемента с индексом {i} {type(my_list[i])}.")
    i += 1
print("Тип всех элементов списка определен.")
