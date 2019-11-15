# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("lesson5z3.txt", "r") as workers_list:
    salary_summ = []
    less_20k = []
    worker = workers_list.read().split("\n")
    for el in worker:
        el = el.split()
        if int(el[1]) < 20000:
            less_20k.append(el[0])
        salary_summ.append(el[1])
    mid_salary = sum(map(int, salary_summ)) / len(salary_summ)
    print(f"Оклад менее 20000 у сотрудников: {less_20k}. Средний доход сотрудика: {mid_salary}.")
