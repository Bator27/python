ip = int(input("Kérem adja meg az ip címének az első negyedét!"))
if ip <= 127:
    print("Az ön ip címe A osztályú!")
elif 128 <= ip <= 191:
    print("Az ön ip címe B osztályú!")
elif 192 <= ip <= 223:
    print("Az ön ip címe C osztályú!")
elif 224 <= ip <= 239:
    print("Az ön ip címe D osztályú!")
elif 240 <= ip <= 255:
    print("Az ön ip címe E osztályú")
else:
    print("Hibás ip cím!")

if ip == 10:
    print("Egy ip privát!")
elif ip == 172:
    print("Tizenhat ip privát!")
elif ip == 192:
    print("ketőszázötvenhat ip privát!")
else:
    print("Az összes ip privát!")
