# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
element = ""
while (element != "exit"):
    element = input("Введите новый элемент списка, для выхода введите exit: ")
    if element == "exit":
        break
    else:
        my_list.append(element)
print(f"Список готов: {my_list}")
i = 0
if len(my_list)%2 == 0:
    while (i < len(my_list)-1):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
else:
    while (i < len(my_list)-2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
print(f"Измененный список готов: {my_list}")