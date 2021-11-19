halmaz = { 'halmazok', 'feladat', 'valami', 'proba','project'}
print(halmaz)
halmaz.clear()
halmaz.copy()

halmaz2 = {'suli', 'project', 'orai' , 'munka'}
halmaz3 = {'A', 'B', 'project'}
print(halmaz2)
print(halmaz2)
halmaz.difference(halmaz2)
halmaz.difference_update(halmaz2)
halmaz.intersection(halmaz2)
halmaz.intersection_update(halmaz2)
halmaz.isdisjoint(halmaz2)

halmaz2.difference(halmaz3)
halmaz2.difference_update(halmaz3)
halmaz2.intersection(halmaz3)
halmaz2.intersection_update(halmaz3)
halmaz2.isdisjoint(halmaz3)

halmaz3.difference(halmaz)
halmaz3.difference_update(halmaz)
halmaz3.intersection(halmaz)
halmaz3.intersection_update(halmaz)
halmaz3.isdisjoint(halmaz)

gaming = {'szamitogep', 'laptop', 'console'}
telefon = {'Samsung','Xiaomi','Huawei', 'Iphone','Alcatel'}
gaming.intersection(telefon)
telefon.intersection(gaming)
gaming.intersection_update(telefon)
telefon.intersection_update(gaming)
gaming = telefon.intersection_update(telefon)
print(gaming)
print(telefon)
print(gaming , telefon)

elsoszamsor = {1,2,3}
masodikszamsor = {4,5,6}

print(elsoszamsor.isdisjoint(masodikszamsor))

harmadikszamsor = {1,2,3,100,11,4}
negyedikszamsor = {1,2,3}

print(negyedikszamsor.isdisjoint(harmadikszamsor))

#issubset
a = {"a", "b", "c"}
b = {"f", "e", "d", "c", "b", "a"}

c = a.issubset(b)
print(c)
#Arra használható,hogy megmondja ,hogy igaz-e a kód
#issuperset() metódus
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Igaz
print(A.issuperset(B))

# Hamis
print(B.issuperset(A))

# Igaz
print(C.issuperset(B))

#Az issuperset() metódus igaz értéket ad vissza, ha egy halmaznak egy másik halmaz minden eleme meg van (argumentumként átadva). Ha nem, akkor False értéket adja vissza.

#symetric_difference
x = {'a', 'b', 'c', 'd'}
y = {'c', 'd', 'e' }
z = {}

print(x.symmetric_difference(y))
print(x.symmetric_difference(y))

print(x.symmetric_difference(z))
print(y.symmetric_difference(z))
#szimetrikusan dolgozik

#len function
stock_price_1 = [50.23]
stock_price_2 = [75.14, 85.64, 11.28]

print('stock_price_1 length is ', len(stock_price_1))
print('stock_price_2 length is ', len(stock_price_2))
#A len() function a lista elemeinek számát mutatja

#count()
#A megadott értékű elemek számát adja vissza
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
print(x)

 #Tuples method
 
t = (2, 4, 6)
print(all(t))
 
t = (0, False, False)
print(all(t))
 

t = (5, 0, 3, 1, False)
print(all(t))
 

t = ()
print(all(t))
