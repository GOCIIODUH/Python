list_nums = [0, -1, 5, 2, 3]
res = [list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]
print(sum(res))