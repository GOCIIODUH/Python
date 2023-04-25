a, b = list(map(int, input("Введите 2 числа через пробел 1-е число, которое будет возводиться в степень, 2-е - степень: ").split()))

def exponentiation(a, b):
    if b == 0: return 1
    if b < 0: return  exponentiation(a, b+1) * 1/a
    return a * exponentiation(a, b-1)

print(exponentiation(a, b))