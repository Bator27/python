indul = int(input("Hány óra a visszaszámlálás?:"))
felfüggesztes = 0

for szam in range(indul,0,-1):
    print("visszaszámlálas", szam)
    valasz = input("Fel kell-e függeszteni? (i/n)")
    if valasz == "i":
        felfüggesztes +=1
print('A rakéta a visszaszámlálást követően ennyi órával indult:', indul + felfüggesztes)
