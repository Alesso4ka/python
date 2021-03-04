#2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#Проверьте его работу на данных, вводимых пользователем.
#При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Division by zero is prohibited")

div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(10, 0.1))


#VAR2
class MyException(Exception):

    def division_func(self, x, y):
        try:
            result = round(x / y, 2)
        except ZeroDivisionError:
            print(f"{x} / {y} -> Division by zero is prohibited!\n")
        else:
            print(f"{x} / {y} = {result} \n")


m_e = MyException()

m_e.division_func(5, 10)
m_e.division_func(1, 0)
m_e.division_func(-6, 3)
m_e.division_func(0, 8)
