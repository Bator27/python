import time

visszaszamlalas = int(input('Kérem adja meg ,hogy hány óra múlva legyen a kilövés!:'))
print(f'A rakéta kilövésig {visszaszamlalas} óra van!')
felfuggesztettórak = 0
elteltorak = 0
hanyelteltora = int(input("Hány eltolt óra lesz?"))
if hanyelteltora > 0:
    visszaszamlalas + hanyelteltora
    print("Visszaszámláláshoz hozzá lesz adva az eltelt órák száma!")
else:
    print("Nem lesz eltolva a kilövés")

"""
I = +1
N = 0
while visszaszamlalas != 0:
    felfuggesztettórak = input(f'A rakéta nem lőhető ki 0 óránál ezt az időt elcsúztatjuk 1 órával: {I} / {N} ?')
    if felfuggesztettórak == ['nem', 'Nem','NEM']:
        visszaszamlalas += 1
        elteltorak += 1
    print('A felfüggesztések miatt a kilővés 1 órával el lett tólva.')
else:
        visszaszamlalas -= 1
        elteltorak = +1
        print(f'A kilövésig {visszaszamlalas} ennyi óra telt el {elteltorak}')
"""

def visszaszámlálás(t):
	
	while t:
		mins, secs = divmod(t, 60)
		visszaszamlalas = '{:02d}:{:02d}'.format(mins, secs)
		print(visszaszamlalas, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Kilövés!!!')
    
#t=time=idő
t = input("Írd be hány óra múlva lesz végül a kilövés?: ")
#Egy másodperc valóságban az itt egy óra
visszaszámlálás(int(t))
time.sleep(3)
print("A rakéta sikeresen kilőve!")
print(f"Felfüggesztett/eltolt órák összesen:{hanyelteltora}")