numbers = list(map(int, input().split()))
max_l = max(numbers)
min_l = min(numbers)
result = [i if i != max_l else min_l for i in numbers]
print(result)

