number = int(input("Введите трехзначное число: "))
if number < 100 or number > 999:
    print("Ошибка: Извините, но Вы ввели не трехзначное число.")
else:
    n3 = number%10
    n2 = number//10%10
    n1 = number//100%10
    print(f"{number} -> {n1+n2+n3} ({n1} + {n2} + {n3})" )