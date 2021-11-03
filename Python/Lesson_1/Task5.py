proseeds = int(input("Введите значение выручки за последний год >>> "))
costs = int(input("Введите значение убытков за последний год >>> "))
if proseeds > costs:
    print(f"Компания прибыльная, рентабельность {proseeds / costs}")
    employees = int(input("Введите количество сотрудников Компании >>> "))
    print(f"Прибыль в расчете на одного сотрудника {proseeds / employees}")
elif proseeds == costs:
    print("Компания работает в ноль")
else:
    print("Компания убыточная")
