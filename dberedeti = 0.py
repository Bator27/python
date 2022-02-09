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