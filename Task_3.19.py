listNums = [1, 2, 3, 4, 5]
k = int(input("Введите k: "))
print(listNums)
for i in range(k):
    listNums.insert(0, listNums.pop())
print(listNums)