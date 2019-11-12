#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.



goods_list = []
exit = ""
goods_dict = {}
while exit != "e":
    goods_index = input("Введите номер товара цифрами: ")
    if goods_index.isdigit():
        name = input("Введите название товара: ")
        price = input("Введите стоимость товара: ")
        number  = input("Введите кол-во товара" )
        goods_dict ={"название" : name, "цена" : price , "количество" : number , "eд": "шт."}
        goods_list.append((int(goods_index), goods_dict))
        exit = input("Для выхода введите e: ")
        break
    else:
        print("Введите номер товара цифрами!")
        continue
print(goods_list)