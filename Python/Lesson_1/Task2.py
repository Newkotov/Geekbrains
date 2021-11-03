second = int(input("Введите количество секунд >>> "))
hours = second // 3600
minutes = (second - hours * 3600) // 60
real_second: int = second - (hours * 3600 + minutes*60)
print("Введенное количество секунд соответствует следующему количеству часов:минут:секунд >>> " f"{hours}:{minutes}:{real_second}") 
