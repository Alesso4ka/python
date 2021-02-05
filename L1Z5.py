#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Enter the revenue value: "))
costs = int(input("Enter the cost value: "))
profit = proceeds - costs
if profit > 0:
    print("The firm is profitable")
    employee = int(input("Enter the number of employees: "))
    profit_per_employee = profit / employee
    print("profit per employee - ", profit_per_employee)
else:
 print("the firm is not profitable")