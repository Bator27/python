#Összegzés - összeadás
t = [ 3, 8, 2, 4, 5, 1, 6]
osszeg = 0
for num in t:
    osszeg=osszeg + num
print("összeg:", osszeg)
print(f"összeg egyenlő {osszeg}")
print(f'összeg egyenlő  {sum(t)}')

#Összegzés - szorzás
osszeg = 1
for num in t:
    osszeg=osszeg * num
print("összeg:", osszeg)
print(f'összeg egyenlő {osszeg}')

#Összegzés - konkatenáció
osszeg = ""
for num in t:
    osszeg = str(osszeg) +str(num)
print("összeg:", osszeg)
print(f'összeg egyenlő {osszeg}')
#Az előző feladat algoritmusát felhasznáéva írjuk meg azt az algoritmust
dberedeti = 0
dbróka = 0
libak = [1 , 5 , 3 , 3 , 4 ]
print(f'Libak sulya {sum(libak)}')
print(f'{len(libak)} libát lopott a rókának')
print(f'átlagos sulya {sum(libak)/len(libak)}')
db=0
rókanak_jut = 0
for liba in libak:
    dberedeti+=1
    if liba<=3:
        rókanak_jut += liba 
        rókanak_jut = rókanak_jut + liba
        dbróka+=1
print(f'A rókanak {rókanak_jut} kg liba jutott')
print(f'Eredeti liba szám {dberedeti} és a rókának {dbróka}')

#Megszámolás
t = [ 3, 8, 2, 4, 5, 1, 6]
count = 0
for num in t:
    if num>5:
        count = count +1
        count +=1
print(f'5-nél nagyobb {count}')
print(len(t))

bevételek = [1,5,2,3,4]
összess = 0

for bevétel in bevételek:

    összes = összes + bevétel
    print('Napi bevétel:', összes, 'picula.')
    print(f'Napi bevétel: {összes} picula.')

összes = sum(bevételek)
print('Napi bevétel:', összes, 'picula.')

bevételek = [1,5,2,3,4]
összes = 0
darab = 0
for bevétel in bevételek:
    összes+= bevétel
    darab += 1
print('Az átlagos bevétel:', összes / darab, 'picula.')