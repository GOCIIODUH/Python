values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
transformation = lambda x: x*2
transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')

print(transformed_values)