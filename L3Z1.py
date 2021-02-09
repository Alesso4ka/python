#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
a = input("Enter value a: ")
while a.isdigit() == False:
    a = input("Enter numerical value a: ")
a = float(a)
b = input("Enter value b: ")
while b.isdigit() == False:
    b = input("Enter numerical value b: ")
b = float(b)
while b == 0: #как тут реализовать защиту от пользователя.
    b = float(input("Division error.The second entered number is zero.Enter another numerical value b: "))
def my_f(a, b):
    return a / b
print(my_f(a, b))

#как сделать защиту от пользователя, который после введения "0" вдруг опять введет букву.
