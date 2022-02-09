t = [3, 8, 2, 4, 5, 1, 6]
n = len(t)
#ker = int(input('Kérem adja me a keresett számot'))
ker = 5

i = 0
while i < n and t[i] != ker:
    i = i + 1

if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)

bevételek = [1, 5, 2, 3, 4]

vanilyen = False
for bevétel in bevételek:
    if bevétel == 5:
        vanilyen = True
        break
    if vanilyen:
        print('Van ötpiculás bevétel.')

if 5 in bevételek:
    print('Van ötpiculás bevétel.')