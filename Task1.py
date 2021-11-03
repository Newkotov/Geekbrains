gender = input("Введите пол >>> ")
gender_list = ["Male", "male", "Female", "female", "M", "m", "F", "f"]

if gender in gender_list:
    print("Спасибо")
else:
    print("Введено неверное значение")
