# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

#не уверена,  что в одну строку записала все правильно.
numbers = range(20, 241)
my_new_list = [el for el in numbers if el%20==0 or el%21==0]
print("Divisors of 20 and 21: ", my_new_list)


print(f"Divisors of 20 and 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}")