import math
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# list

list_month = ["зима", "лето", "весна", "осень"]
user_month = int(input("Введи месяц числом от 1 до 12: "))
if 1 <= user_month <=2 or user_month == 12:
    print(f"{user_month} месяц это {list_month[0]}.")
elif 3 <= user_month <= 5:
    print(f"{user_month} месяц это {list_month[2]}.")
elif 6 <= user_month <= 8:
    print(f"{user_month} месяц это {list_month[1]}.")
elif 9 <= user_month <= 11:
    print(f"{user_month} месяц это {list_month[3]}.")
else:
   print("Введите число от 1 до 12!")


# dict

dict_month = {(1, 2, 12):'зима', (3, 4, 5):'весна', (6, 7, 8):'лето', (9, 10, 11):'осень'}
user_month = ''
list_keys = list(dict_month.keys())
def month_sort (x):
    for i in list_keys[x]:
        if user_month == i:
            print(dict_month.get(list_keys[x]))
            break
        else:
            continue

while (user_month != 0):
    user_month = input("Введи месяц числом от 1 до 12(для выхода введите цифру 0): ")
    if user_month.isdigit():
        user_month = int(user_month)
        if (1 <= user_month <= 12):
            month_sort(0)
            month_sort(1)
            month_sort(2)
            month_sort(3)
        elif user_month == 0:
            print("Программа завершена")
            break
        else:
            print("Введите число от 1 до 12!")
            continue
    else:
        print("Введите число от 1 до 12!")
        continue


