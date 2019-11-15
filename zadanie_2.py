# Перевод секунд в формат чч:мм:сс.

number = int(input("Сколько секунд нужно перевести?"))
hour = number // 3600
min = (number - hour * 3600) // 60
sec = number - hour * 3600 - min * 60
date = "{} секунд - это {}h:{}m:{}s".format(number, hour, min, sec)
print(date)


