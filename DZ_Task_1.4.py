n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
if k < n * m and (k % n == 0 or k % m == 0):
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")