# Найти самую большую цифру в числе.

numbers = int(input())
max = numbers%10
numbers = numbers//10
while numbers > 0:
    if numbers%10 > max:
        max = numbers%10
    numbers = numbers//10
print(max)
