a = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите количество элементов арифметической прогрессии: "))

arithmeticProgression = list()
for i in range(n):
    arithmeticProgression.append(a + i * d)
print(arithmeticProgression)