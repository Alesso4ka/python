#Пользователь вводит время в секундах.Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк

Time = int(input("Enter your time in seconds: "))
Hours = Time // 3600
Remainder_of_division = Time % 3600
Minutes = Remainder_of_division // 60
Seconds = Remainder_of_division % 60
print(f"Time is hh:mm:ss - {Hours} : {Minutes} : {Seconds}")
