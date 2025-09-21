# ввести швидкість автомобіля
speed = int(input())

# Визначити проміжки часу
time_intervals = [6, 10, 15]

# Р70озрахувати відстань
for time in time_intervals:
    distance = speed * time
    print(distance)