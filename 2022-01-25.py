import math
from re import A

haromszog = [3,4,5]
print(haromszog)
ker = 0 
for i in haromszog:
    ker = ker + i
    print(ker)

kerulet = sum(haromszog)
print(kerulet)

s = ker/2
terulet = s * math.sqrt((s-haromszog[0])* (s-haromszog[1])* (s-haromszog[2]))
print(f'A haromszognek a terulete : {terulet}')

wr = open("haromszog.txt", 'w')
wr.write(f'A haromszognek a terulete : {terulet}')
wr.close()


#haromszog = [3, 4, 5]

#keres = 4
wr = open('haromszog.txt', 'a')
keres = int(input("addjon meg egy számot!"))
vanilyen = None
# a = len(haromszog)
for index in range(len(haromszog)):
    if haromszog[index] == keres:
        vanilyen = True
        holvan = index
        break
if vanilyen:
    print(f'sorszáma , {holvan +1}')
    wr.write(f'\n sorszáma , {holvan +1}')
else:
    print("nincs")

if keres in haromszog:
    print(f'a keresett szám sorszáma {haromszog.index(keres)+ 1}')
    wr.write(f'\n a keresett szám sorszáma {haromszog.index(keres)+ 1}')
else:
    print (f'nincs')

#haromszog = [3,4,5]
max = 0

for oldal in haromszog:
    if oldal > max:
        max = oldal
print(f'a legnagyobb oldal mérete: {max}')

wr.write(f'\na legynagyobb oldal mérete: {max}')

min = haromszog[0]
for oldal in haromszog:
    if oldal < min:
        min = oldal
print(f'a legkisebb oldal mérete: {min}')

wr.write(f'\na legykisebb oldal mérete: {min}')

wr.close()