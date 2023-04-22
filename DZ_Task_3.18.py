# Если два числа равноудалены от введенного, то выводим меньшее
import random
rand = [random.randint(0, 100) for i in range(int(input("Введите количество элементов: ")))]
print(rand)
x = int(input("Введите число для анализа: "))
min = 10000
for i in range(len(rand)):
    if abs(x - rand[i]) < min and x - rand[i] != 0:
        min = abs(x - rand[i])
    i += 1
print(x-min)