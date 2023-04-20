n = int(input("Введите количество арбузов: "))
max= 0
min = 100
for i in range(n):
    count = int(input(f"{i+1}-арбуз: "))
    if count > max:
        max = count
    if count < min:
        min = count
print(f"Max={max}, Min={min}")