# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(*args):
    user_dict = {"Имя" : name, "Фамилия" : second_name , "ГР" : number , "Город": city}
    for key, value in user_dict.items():
        print(key, ':', str(value))

name = input("Введите имя: ")
second_name = input("Введите фамилию: ")
number = input("Введите ГР: ")
city = input("Введите город проживания: ")

user_info(second_name, city, number, name)