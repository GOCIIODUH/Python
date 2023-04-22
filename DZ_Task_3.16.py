import random
rand = [random.randint(0, 9) for i in range(int(input("Введите количество элементов: ")))]
print(rand)
x = int(input("Введите число для анализа: "))
a = 0
for i in range(len(rand)):
    if rand[i] == x: a += 1
    i += 1
print(a)
