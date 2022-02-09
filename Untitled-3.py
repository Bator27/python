from os import kill


wr = open("liba2.txt", 'w')
libak = [1,5,2,3,4]
vanilyen = False
for index in range(len(libak)):
    wr.write(str(libak))
    if index > 0:
        if libak[index] <libak[index-1]:
            vanilyen = True
            break
    if vanilyen:
        print('Volt, amikor kisebb libát lopott az előző napnál.')

wr.write('Volt, amikor kisebb libát lopott az előző napnál.')
wr.close()
wr = open("liba2.txt", "a")
wr.write("\nDávid")
wr.close()