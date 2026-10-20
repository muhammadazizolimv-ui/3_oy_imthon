a = {"olma": 5000, "banan": 12000}
b = {"banan": 15000, "anor": 10000}

for key in b:
    a[key] = b[key]

print(a)
