"""
#kitérő: egy változóba (nem listába) kerül az egész hóbelevanc
forrásfájl = open('raspberries.txt')
print(forrásfájl.read())
forrásfájl.close()

#kitérő:
print('Karakterenként')
import time forrásfájl = open('raspberries.txt')
while True:
    betű = forrásfájl.read(1)
    if betű:
        #print(forrásfájl.tell())
        print(betű, end='')

"""