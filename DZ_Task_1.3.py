number = int(input("Введите номер билета: "))
n1 = number//1000
n11 = n1 % 10
n12 = n1 // 10 % 10
n13 = n1 // 100 % 10

n2 = number - n1 * 1000
n21 = n2 % 10
n22 = n2 // 10 % 10
n23 = n2 // 100 % 10    

if n11 + n12 + n13 == n21 + n22 + n23:
    print(f"{number} -> yes")
else:
    print(f"{number} -> no")

# sum1 = 0
# sum2 = 0
# while n1 > 0:
#     sum1 += n1 % 10
#     n1 = n1 // 10
#     sum2 += n2 % 10
#     n2 = n2 // 10
# if sum1 == sum2:
#     print(f"{number} -> yes")
# else:
#     print(f"{number} -> no")
