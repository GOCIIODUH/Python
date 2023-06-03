song = list(input('Введи стих, Винни: ').lower().split())
def definitionRhyme(list):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    quantity = []
    for word in list:
        sum = 0
        for i in word:
            if i in vowels:
                sum += 1
        quantity.append(sum)
    if len(quantity) == quantity.count(quantity[0]) and all(quantity):
        print('Парам пам-пам')
    else:
        print('Пам парам')

definitionRhyme(song)