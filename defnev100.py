#1
from re import X


def nev(n):
    if n != 0:
        nev(n-1)
        print("Dávid")
nev(100)
#2
def abakóba_vált(liter):
    return liter/58.6

print('999 liter az', abakóba_vált(999),'akó.')

#3
def betűkkel(szám):
    számok_nevei = ['nulla','egy','kettő','három','négy','öt','hat','hét','nyolc','kilenc']
    return számok_nevei[szám]

for szám in range(10):
    print(szám, betűkkel(szám))

#4
szo = input('Kérem adjon meg egy szót!')
def névelő(szó):
    magánhangzók = ['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']
    if szó[0] in magánhangzók:
        return 'az'
    else:
        return 'a'
print(névelő(szo), szo)
#5
def hangrend(szó):
    mély_magánhangzók = ['a','á','o','ó','u','ú']
    magas_magánhangzók = ['e','é','i','í','ö','ő']
    volt_mély = False
    volt_magas = False
    for betű in szó:
        if betű in mély_magánhangzók:
            volt_mély = True
        elif betű in magas_magánhangzók:
            volt_magas = True
    if volt_mély and not volt_magas:
        return('mély')

    elif not volt_mély and volt_magas:
        return('magas')
    elif volt_mély and volt_magas:
        return('vegyes')
    else:
        return('nincs magánhangzó')

szó = input('Írj ide egy szót! ')
print(hangrend(szó))
    
def monogramm(nev):
    szoköz = nev.index('')
    return nev[0] + '.' + nev[szoköz+1]

nev = input('Kérem adj meg a nevét')
print(monogramm(nev),nev)
