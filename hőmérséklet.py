wr = open("hom.txt", "w")
hom = [9,-16,-19,-8,-2,14,15,16,-8,8,-3,-9,-4,-3,18,-17,-7,-1,7,10,-12,14,7,6,-6,-20,10,3]

i = -2

for i in hom:
    if i in hom:
        print(f'Volt -2 fok')
        #print(len(i in hom))
        wr.write(f'Volt -2 fok')
    else:
        print(f'Nem volt -2 fok')


összhom = sum(hom)
print(f'Az összhőmérséklet: {összhom}')
wr.write(f'\nAz összhőmérséklet: {összhom}')
átlag = (összhom / 28)
print(f'Az átlag hőmérséklet: {átlag}')
wr.write(f'\nAz átlag hőmérséklet: {átlag}')
minhom = min(hom)
print(f'A minimum hőmérséklet: {minhom}')
wr.write(f'\nA minimum hőmérséklet: {minhom}')
maxhom = max(hom)
print(f'A max hőmérséklet: {maxhom}')
wr.write(f'\nA max hőmérséklet: {maxhom}')
lenhom = len(hom)
print(f'A len hőmérséklet: {lenhom}')
wr.write(f'\nA len hőmérséklet: {lenhom}')
hőinghom = (maxhom-minhom)
print(f'A hőingadozás különbsége: {hőinghom}')
wr.write(f'\nA hőingadozás különbsége: {hőinghom}')

wr.close