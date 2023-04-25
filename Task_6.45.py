# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
# def mult(num):
#     sum = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0: 
#             sum += i
#     return sum
# number = (int(input('Введите число: ')))
# for i in range(number):
#     j = mult(i)
#     if i < j < number and i == mult(j):
#         print(i, j)


def pair(value):
    # Получаем корень числа, отбрасываем дробную часть
    sq_num = int(value ** 0.5)

    # Выставляем начальное значение в переменной
    # Если переменная sq_num возведённая в квадрат
    # не равна полученному числу, прибавляем 0.
    # Иначе прибавляем это число, т.к. оно тоже множитель
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    # Цикл от 2 др корня числа
    for i in range(2, sq_num):

        # Если полученное число делиться на i без остатка
        if value % i == 0:
            # Складываем в переменную значение i
            # и второй делитель, например
            # value = 10, i = 2, второй делитель 5
            res += i + value // i
    return res


for j in range(10, 300):
    # Первое число, это сумма множителей j
    sum1 = pair(j)

    # Второе число, это сумма множителей sum1
    sum2 = pair(sum1)

    # Если второе число равно j и первое число меньше второго
    # Второе условие защита от дубликатов,
    # записанных наоборот
    if sum2 == j and sum1 < sum2:
        print(j, sum1)
