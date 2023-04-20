number = int(input("Введите N: "))
i = 1
fakt = 1
while i <= number:
    fakt *= i
    i += 1
print(fakt)