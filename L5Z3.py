#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.
with open("L5Z3.txt", "r") as my_file:
    rich = []
    poor = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        rich.append(i[1])
print(f"Salary less 20.000 {poor}, Middle salary {sum(map(float, rich)) / len(rich)}")