list1 = [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
list2= [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
list3= [i for i in list1  if i not in list2]

print(list1)
print(list2)
print(list3)
