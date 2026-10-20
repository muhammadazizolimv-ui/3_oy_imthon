def tahlil_qil(sonlar):
    juft_yigindi = 0
    toq_yigindi = 0
    eng_katta = sonlar[0]

    for son in sonlar:
        if son % 2 == 0:
            juft_yigindi += son
        else:
            toq_yigindi += son

        if son > eng_katta:
            eng_katta = son

    print(f"Juft sonlar yig'indisi: {juft_yigindi}")
    print(f"Toq sonlar yig'indisi: {toq_yigindi}")
    print(f"Eng katta son: {eng_katta}")


sonlar = [12, 7, 5, 18, 9, 4]
tahlil_qil(sonlar)
