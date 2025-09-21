# вхідне дійсне число (кут годинникової стрілки)
a = float(input())

# Розраховуємо загальну кількість годин з початку доби
total_hours = a / 30

# Визначаємо кількість хвилин, що пройшли в межах поточної години
minutes_in_current_hour = (total_hours - int(total_hours)) * 60

# Обчислюємо кут повороту хвилинної стрілки
minute_hand_angle = minutes_in_current_hour * 6

# Виводимо результат
print(minute_hand_angle)