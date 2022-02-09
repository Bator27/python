#Összegzés - összeadás
t = [ 3, 8, 2, 4, 5, 1, 6]
osszeg = 0
for num in t:
    osszeg=osszeg + num
print("összeg:", osszeg)
print(f"összeg egyenlő {osszeg}")
print(f'összeg egyenlő  {sum(t)}')

t = [ 3, 8, 2, 4, 5, 1, 6]
count = 0
for num in t:
    if num>5:
        count = count +1
        count +=1
print(f'5-nél nagyobb {count}')
print(len(t))