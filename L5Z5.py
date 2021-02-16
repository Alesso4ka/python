#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    try:
        with open("L5Z5.txt", "w+") as file_obj:
            line = input("Enter numbers separated by a space: \n")
            file_obj.writelines(line)
            my_n = line.split()

            print(sum(map(int, my_n)))
    except IOError:
        print("File error")
    except ValueError:
        print("Wrong number. Input/Output error")
summary()