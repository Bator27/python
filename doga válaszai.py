import random

wr = open("fa.txt", "w")
fa = []
szam = 0
while szam != 31:
    kitermeles = random.randint(50,100)
    fa.append(kitermeles)
    szam += 1

össz = 0
for megtermelt in fa:
    össz += megtermelt
print(f"A márciusi összes fatermelés {össz}")
wr.write(f"A márciusi összes fatermelés {össz} m3")
"""
össz = sum(fa)
"""
átlag = össz/ len(fa)
print(f"A márciusi kitermelt fa átlaga: {átlag}")
wr.write(f"\nA márciusi kitermelt fa átlaga: {átlag}")
legkisebb = min(fa)
legnagyobb = max(fa)
"""
for i in fa:
    if i < legkisebb:
        legkisebb = i
    elif i > legnagyobb:
        legnagyobb = i
"""
print(f"A legkisebb {legkisebb} volt, a legnagyobb {legnagyobb}")
wr.write(f"\nA legkisebb {legkisebb} volt, a legnagyobb {legnagyobb}")

if 40 in fa:
    print("Volt olyaan nap, ahol 41 volt a kitermelt fa")
    wr.write("\nVolt olyan nap , ahol 40 volt a kitermelt fa")
else:
    print("Nem volt olyaan nap, ahol 41 volt a kitermelt fa")
    wr.write("\nNem olt olyan nap , ahol 40 volt a kitermelt fa")

van40= False
for x in fa:
    if x == 40:
        print("Van ilyen")
        van40 = True
        break
    else:
        print("Nincs ilyen")

nagy_termeles_szama = 0
nagy_termeles_összege = 0
for x in fa:
    if x > 70:
        nagy_termeles_szama +=1
        nagy_termeles_összege += x
print(f"{nagy_termeles_szama} alkalommal volt 70 feletti a nap termeles")
print(f"A 70 feletti termelések összege {nagy_termeles_összege}")
wr.write(f"\n{nagy_termeles_szama} alkalommal volt 70 feletti a nap termeles")
wr.write(f"\nA 70 feletti termelések összege {nagy_termeles_összege}")

ossztermeles_szazaleka = nagy_termeles_összege/ossz*100
wr.close()