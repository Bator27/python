def megítél (mondat):
    if len (mondat) > 0:
        if mondat[-1] != '!' and mondat[-1] != '?' and mondat[-1] != '.':
            print('Hát ejnye!')
        else:
            print('Igazán gyönyörű mondat!')

mondat = None
while mondat != '':
    mondat = input('Írj ide egy mondatot!')
    megítél(mondat)