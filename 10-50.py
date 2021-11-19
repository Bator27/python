import random 

szam = random.randrange(10,50)
szam2 = random.randrange(10)
lista1 = [szam , szam2]
lista2 = []
for i in lista1:
    print(i)
print( "for ciklus" )
print(szam)
print(szam2)
while szam2>szam:
    szam = random.randrange(10,50)
if szam < szam2:
    a = (szam/szam2)
    b = (szam//szam2)
    c = (szam%szam2)
else:
    a = (szam2/szam)
    b = (szam2//szam)
    c = (szam2%szam)
lista2.append(a)
lista2.append(b)
lista2.append(c)
lista2.sort()
print(lista2)
