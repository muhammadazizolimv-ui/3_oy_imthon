matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

yigindi = 0

for qator in matritsa:
    for element in qator:
        yigindi += element

print(f"Matritsa elementlar yig'indisi==: {yigindi}")
