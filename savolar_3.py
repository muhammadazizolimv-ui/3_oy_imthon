mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

mahsulot_nomi = input("Mahsulot nomini kiriting: ")
yangi_narx = int(input("Yangi narx: "))

if mahsulot_nomi in mahsulotlar:
    mahsulotlar[mahsulot_nomi] = yangi_narx
    print("kirtlgan narh yangiladni==")
    print(mahsulotlar)
else:
    print("siz kirtgan mahsulot topildi==")
