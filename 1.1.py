"""
Задача №1

Автомобіль може проїхати відстань n кілометрів за день.
Скільки днів пройде для проїзду маршруту довжиною m кілометрів?
Програма отримує два цілих додатних числа: n і m. Результат має бути також цілим числом.

Виконала: Гриб Наталія Григорівна, 31І група
"""

n = int(input("Введіть відстань, яку може проїхати автомобіль за день (км): "))
m = int(input("Введіть загальну відстань маршруту (км): "))

days = m//n

print ("Пройде", days, "днів")
