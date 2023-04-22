# A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т– 1 очко;
# D, G, Д, К, Л, М, П, У – 2 очка;
# B, C, M, P, Б, Г, Ё, Ь, Я – 3 очка;
# F, H, V, W, Y, Й, Ы – 4 очка;
# K, Ж, З, Х, Ц, Ч – 5 очков;
# J, X, Ш, Э, Ю  – 8 очков;
# Q, Z, Ф, Щ, Ъ – 10 очков.

dictionary = {1 : "[AEIOULNSTRАВЕИНОРСТ]", 2 : "[DGДКЛМПУ]", 3 : "[BCMPБГЁЬЯ]", 4 : "[FHVWYЙЫ]", 5 : "[KЖЗХЦЧ]", 8 : "[JXШЭЮ]", 10 : "[QZФЩЪ]"}
text = input("Введите слово: ").upper()
summ = 0
for i in text:
    for k, v in dictionary.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")