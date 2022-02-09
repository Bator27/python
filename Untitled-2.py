wr = open("liba.txt", 'w')
libak = [1 , 5 , 2 , 3 , 4 ]
vanilyen = False
for liba in libak:
    wr.write(str(liba))
    if liba >= 3:
        vanilyen = True
        break
if vanilyen:
    print('Van legalább egy háromkilós liba.')
    wr.write('\nVan legalább egy három kilós liba!')
wr.close
wr = open("liba2.txt", 'w')
vanilyen = False
for index in range(len(libak)):
    wr.write(str(index))
    if index > 0:
        if libak[index] <libak[index-1]:
            vanilyen = True
            break
        if vanilyen:
            print('Volt, amikor kisebb libát lopott az előző napnál.')
            wr.write('Volt, amikor kisebb libát lopott az előző napnál.')
wr.close