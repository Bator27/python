#zsák
wr = open('zsak.txt', 'w')
zs = [2,9,19,20,5,7,11]
total = sum(zs)
darab = len(zs)
atlag = total/darab
print(f'Átlag:{atlag}')
wr.write(f' Átlag:{atlag}')
print(f'Darab: {darab} ')
wr.write(f'\n Darab: {darab} ')
print(f'A zsák össztömege {total} kg')
wr.write(f'\n A zsák össztömege {total} kg')
db = 0
for i in zs:
    if i>5:
        db+=1
print(f'A listában ötnél nagyobb számok száma: {db}')
wr.write(f'\n A listában ötnél nagyobb számok száma: {db}')
n = len(zs)
ker = 5
i = 0
while i < n and zs[i] !=ker:
    i = i + 1

if i<n:
    print("Van ilyen az ötödik helyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)

wr.close()