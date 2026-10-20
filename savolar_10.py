from matplotlib import pyplot
kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

pyplot.plot(kunlar,daromad,label="daromadlar",color="red",linestyle="--",marker="o")
pyplot.title("hada haftalik daromadlar")
pyplot.ylabel("daromadlar")
pyplot.xlabel("hafta kunlari")
pyplot.grid(True)
pyplot.legend()
pyplot.savefig("daromad.png")