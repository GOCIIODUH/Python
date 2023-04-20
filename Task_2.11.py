number = int(input("Введите число: "))
i = 0
j = 1
count = 2

while j <= number:          
    if j == number:
        print(count)
        break
    i, j = j, i + j
    count += 1
else:
    print(-1)
