import math

a = float(input('Kérem a másodfokú egyenlet:'))

while a==0:
    print('Ez nem lesz másodfokú egyenlet')
    a= input('Kérem a konstans tagot')
    a= float(a)

b= float(input('Kérem a másodfokú egyenlet együtt hatóját!: '))
c= float(input ('A diszkrimináns tagot'))
d= b*b-4*a*c
print(d)
if d >= 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
    print('Van valós megoldás')

else:
    x1 = (-b+math.sqrt)(d)/(2*a)
    x2 = (-b-math.sqrt)(d)/(2*a)
    print(x1)
    print(x2)
    print('Nincs valós megoldás')