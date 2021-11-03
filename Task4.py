numeral = abs(int(input("Введите целое положительное число >>> ")))
number = numeral % 10
while numeral >= 1:
    numeral = numeral // 10
    if numeral % 10 > number:
        number = numeral % 10
    if numeral > 9:
        continue
    else:
        print("Максимальное цифра в числе ", number)
        break