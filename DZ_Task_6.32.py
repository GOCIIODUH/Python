# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7 (Для проверки (5, 15)) -> [1, 9, 13, 14, 19]
arr = list(map(int, input("Введите массив через пробел: ").split()))
print (arr)

low, top = list(map(int, input("Введите диапазон фильтра для массива через пробел: ").split()))

newArr = list()

for i in range(len(arr)):
    if low <= arr[i] <= top:
        newArr.append(i)

print(newArr)