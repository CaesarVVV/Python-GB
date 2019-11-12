# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

i = 0
rand_list = [1, 6, 3, 4, 12, 8]
new_list = []
while i < len(rand_list) - 1:
    if rand_list[i] > rand_list[i - 1]:
        new_list.append(rand_list[i])
        i += 1
    else:
        i += 1
        continue
new_list2 = [el for num, el in enumerate(rand_list) if rand_list[num] > rand_list[num - 1]]
print(rand_list)
print(new_list)
print(new_list2)
