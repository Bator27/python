wr = open("liba.txt", 'w')
dberedeti = 0
dbróka = 0
libak = [1 , 5 , 2 , 3 , 4 ]
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

vanilyen = False
for liba in libak:
    wr.write(liba)
    if liba >= 3:
        vanilyen = True
        break
if vanilyen:
    print('Van legalább egy háromkilós liba.')
    wr.write('Van legalább egy három kilós liba!')

vanilyen = False
for index in range(len(libak)):
    if index > 0:
        if libak[index] <libak[index-1]:
            vanilyen = True
            break
        if vanilyen:
            print('Volt, amikor kisebb libát lopott az előző napnál.')
wr.close()