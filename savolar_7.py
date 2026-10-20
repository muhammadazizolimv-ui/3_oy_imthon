import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5],
    ["Shakar", 18000, 15]
]

with open("mahsulotlar.csv", "w", newline="") as f:
    yozuvchi = csv.writer(f)
    yozuvchi.writerow(["nom", "narx", "soni"])
    yozuvchi.writerows(mahsulotlar)

print("mahsulotlar.csv fayliga yozildi.")

