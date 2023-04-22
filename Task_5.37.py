def num_s(n):
    if n == 0:
        return ''
    res = input()
    return num_s(n - 1) + f'{res} '

print(num_s(5))
