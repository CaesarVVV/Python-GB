# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("lesson5z5.txt", "w+") as my_file:
    numbers = input("Введите числа через пробел: ")
    my_file.write(numbers)
    my_file.seek(0)
    line = my_file.read().split()
    for i in line:
        sum_numbers = sum(map(int, line))
    print(f"Сумма чисел в файле: {sum_numbers}.")
