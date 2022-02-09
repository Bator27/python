import random

nev = input("Kérem adja meg a nevét!")
szam1 = int(input("Kérem adjon meg egy számot!"))
while szam2%2 == 1:
    szam2 = random.randrange(10,50)
    print(szam1)
    print(szam2)

szam3 = 5
#halmaz
szamok2 = {23}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(szam3)
print(szamok2)
#szamok2[0] = szam1
#lista
szamok = [10]
szamok.add(szam1)
szamok.add(szam2)
szamok.add(szam3)

print(szamok)

szamok.append(szam1)
szamok.append(szam2)
szamok.append(szam3)

print(szamok)


if szam1  %2 == 0:
    print("Páros")
else:
    print("páratlan")


wr = open("david.txt" , 'w')
wr.write(nev)
wr.write("\nszam4")
wr.close()

lista = [1,2,3,4,5,"abc","def"]
with open('Dávid2.txt', 'w') as file:
    for item in lista:
        file.write("%s\n" % item)

f = open("Dávid2.txt")
tartalom = f.read()
print(tartalom)


gyomulcsok = ["eper","barack","ananász"]
print(f'A gyümölcsök nevű lista következőket tartalmazza:{gyomulcsok}')
for (i,y)  in enumerate (gyomulcsok):
    print(i,y)

print("".join)
f.close()
