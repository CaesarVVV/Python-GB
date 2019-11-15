# Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("lesson5z4answer.txt", "a") as new_file:
    with open("lesson5z4.txt") as stock_file:
        line = stock_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dict[i[0]] + " - " + i[1] + "\n")
