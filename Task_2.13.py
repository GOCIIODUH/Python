n = int(input("Введите N: "))
count = 0
tmp = 0
for i in range(n):
    temp = int(input(f"{i+1}-день: "))
    if temp > 0:
        count +=1
        if count > tmp:
            tmp = count
    else:        
        count = 0
print(tmp)