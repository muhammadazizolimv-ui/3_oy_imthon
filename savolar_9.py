def tashqi(koeffitsiyent):
    def ichki(qiymat):
        return qiymat * koeffitsiyent
    return ichki

koeffitsiyent = 4
qiymat = 7
natija = tashqi(koeffitsiyent)(qiymat)

print(f"Natija: {natija}")
