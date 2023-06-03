values = [1, 1, 1, 1]


def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')