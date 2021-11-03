number = int(input("Введите произвольное число от 1 до 10 >>> "))
total = (number+int(str(number)+str(number))+int(str(number)+str(number)+str(number)))
if number > 10:
    print("Вы ввели некорректное число")
else:
    print("Сумма равна >>> " f"{number}+{number*2}+{number*3}={total}")
