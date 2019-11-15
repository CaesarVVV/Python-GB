# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
lines_number = 0
content = None
with open("lesson5z2.txt", "r+") as my_file:
    while True:
        content = my_file.readline()
        if content != '':
            words_number = len(content.split())
            lines_number += 1
            print(f"В строке {lines_number} кол-во слов равно {words_number}")
        else:
            break
print(f"Общее кол-во строк: {lines_number}")
