numberCranes = int(input("Введите общее количество сделанных журавликов: "))
if numberCranes % 6 == 0:
    print(f"{numberCranes} -> {numberCranes//6} {numberCranes//3*2} {numberCranes//6}")
else:
    print("Ошибка: Невозможно распределить поровну.")