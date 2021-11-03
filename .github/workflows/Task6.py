first_day_mileage = float(input("Введите результат пробежки в первый день >>> "))
goal = int(input("Введите целевой километраж >>> "))
total_mileage = first_day_mileage
achive_day = 1
while total_mileage < goal:
    first_day_mileage = first_day_mileage + first_day_mileage * 0.1
    achive_day += 1
    total_mileage = total_mileage + first_day_mileage
    print(f"Вы достигните цели на {achive_day} день")