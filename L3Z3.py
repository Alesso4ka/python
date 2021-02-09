#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
a = input("Enter the first number: ")
while a.isdigit() == False:
    a = input("Enter numerical value a: ")
a = float(a)
b = input("Enter the second number: ")
while b.isdigit() == False:
    b = input("Enter numerical value b: ")
b = float(b)
c = input("Enter the third number: ")
while c.isdigit() == False:
    c = input("Enter numerical value c: ")
c = float(c)
def my_f(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print(f"Result summ: ", my_f(a, b, c))

