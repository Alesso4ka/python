#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
a = input("Enter name: ")
b = input("Enter sname: ")
c = input("Enter year of birth: ")
d = input("Enter city of residence: ")
e = input("Enter email: ")
f = input("Enter phone: ")
def func(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f"name - {var_1}; sname - {var_2}; year of birth - {var_3}; city of residence - {var_4}; email - {var_5}; phone -{var_6}")
func(var_1=a, var_2=b, var_3=c, var_4=d, var_5=e, var_6=f)

