arrPemenang = []


tim1 = input("Klub A: ")
tim2 = input("Klub B: ")


still_go = False
i = 1
while not still_go:
    skorA, skorB = map(int,input("pertandingan ke-{}: ".format(i)).split())
    if skorA == -1 or skorB == -1:
        still_go = True
    else:
        if skorA > skorB:
            arrPemenang.append(tim1)
        elif skorA < skorB:
            arrPemenang.append(tim2)
        else:
            arrPemenang.append("DRAW")
        i += 1
for i,val in enumerate(arrPemenang,1):
    print("Hasil {}: {}".format(i,val))
