# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input("Enter positive integer number: "))
max = 0
while n:
    h = n % 10
    if h > max:
        max = h
        if max == 9:
            break
    n = n // 10
print("The larges digit is ", max)

