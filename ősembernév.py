nev = input('Adj meg egy ösember nevet!')
print(nev)

bogyok = int(input('Kerem adja meg, hogy mennyi bogyoja van'))

if bogyok < 10:
    minosites = 'Zsenge/noob'
elif bogyok > 20:
    minosites = 'nagy koponya/profi'
else:
    minosites = 'gyujtogeto'


print(f'{nev}, egy {minosites}.')