# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    result_1 = x + y
    result_2 = x + z
    result_3 = y + z
    if result_1 > result_2:
        return  result_1
    elif result_2 > result_3:
        return result_2
    else:
        return result_3


user_list = input("Ввчеди числа через пробле: ").split()
print (my_func(x, y, z))

