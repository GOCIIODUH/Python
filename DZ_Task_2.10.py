n = int(input("Введите количество монет: "))
n0 = 0
n1 = 0
for i in range(n):
    count = int(input(f"{i+1}-монета: "))
    if count == 0: n0 += 1
    else: n1 += 1
if n0 > n1: print(n1)
else: print(n0)