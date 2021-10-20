a = "Hellp , World! "
print(a.split(";"))

a = "Helló"
b = "World"
c = a + b
print(c)
print(a+" " + b)

a = "Helló"
b = "World"
c = a + " " + b
gyumolcs = "banán"
m = gyumolcs[1]
print(m)

m = gyumolcs[0]
print(m)

gyumolcs = "banán"
lista = list(enumerate(gyumolcs))
print(lista)

primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
p4 = primek[4]
print(p4)

baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
b3 = baratok[3]
print(b3)

gyumolcs = "banán"
hossz = len(gyumolcs)
print(hossz)

sz = len(gyumolcs)
utolso = gyumolcs[sz-1]
print(utolso)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1 #i=i+1 csak elvan hagyva a második i
    #bejárás és for
for c in gyumolcs:
    print(c)

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur" , "szakáll" ]

for utotag in utotagok_listaja:
    print(elotag + utotag)

s = "A Karib-tenger kalózai"
print(s[0:1])  #A
print(s[2:14]) #Karib-tenger
print(s[15:22])#kalózai

gyumolcs = "banán"
gy = gyumolcs[:3]
print(gy)   #ban
gy = gyumolcs[3:]
print(gy)   #án
gy = gyumolcs[3:999]
print(gy)   #án
 
#keresünk egy szót
txt = "Helló, welcome to my world."
x = txt.find("welcome")
y = txt.find("w")
print(x)

nev = "Alice"
kor = 10
s2 = "A nevem {1}, és {0} éves vagyok.".format(kor, nev)
print(s2)

n1 = 4
n2 = 5
