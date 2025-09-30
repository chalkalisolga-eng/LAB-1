# Ввід дійсного додатного числа
number = float(input("Введіть додатне дійсне число: "))

# Знаходимо дробову частину
fractional_part = number - int(number)

# Вивід результату
print(f"Дробова частина числа: {fractional_part:.3f}")
