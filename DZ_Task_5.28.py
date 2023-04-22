a, b = list(map(int, input("Введите 2 числа для их сложения через пробел: ").split()))

def summa(a, b):
    if a > b:
        if b == 0: return a
        return summa(a+1, b-1)
    else:
        if a == 0: return b
        return summa(a-1, b+1)

print(summa(a, b))