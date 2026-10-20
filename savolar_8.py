import json

with open("products.json", "r") as f:
    mahsulotlar = json.load(f)

mahsulot_nomi = input("Mahsulot nomi: ")
yangi_miqdor = int(input("Yangi miqdor: "))

for mahsulot in mahsulotlar:
    if mahsulot["nom"] == mahsulot_nomi:
        mahsulot["miqdor"] = yangi_miqdor
        break
else:
    print("Mahsulot topilmadi.")
  

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(mahsulotlar, f, ensure_ascii=False, indent=4)

print("Yangilangan ma'lumot saqlandi.")
