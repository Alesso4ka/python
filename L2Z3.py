#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

#вариант решения через list.
seasons = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Enter the month number: "))
if month == 1 or month == 2 or month == 12:
    print("The entered number refers to the season:", seasons[0])
elif month == 3 or month == 4 or month == 5:
    print("The entered number refers to the season:", seasons[1])
elif month == 6 or month == 7 or month == 8:
    print("The entered number refers to the season:", seasons[2])
elif month == 9 or month == 10 or month == 11:
    print("The entered number refers to the season:", seasons[3])
else:
    print("You are wrong, there is no such month and season")

#вариант решения через dict.
seasons = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Enter the month number: "))
if month == 1 or month == 2 or month == 12:
    print("The entered number refers to the season:", seasons.get(1))
elif month == 3 or month == 4 or month == 5:
    print("The entered number refers to the season:", seasons.get(2))
elif month == 6 or month == 7 or month == 8:
    print("The entered number refers to the season:", seasons.get(3))
elif month == 9 or month == 10 or month == 11:
    print("The entered number refers to the season:", seasons.get(4))
else:
    print("You are wrong, there is no such month and season")