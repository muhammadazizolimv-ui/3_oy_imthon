talabalar = [("Ali", 85), ("Malika", 95), ("Vali", 78)]

yuqori_ballilar = []
for ism, ball in talabalar:
    if ball >= 0:
        yuqori_ballilar.append((ism, ball))
saralangan = sorted(yuqori_ballilar, key=lambda a: a[1])

print(saralangan)
