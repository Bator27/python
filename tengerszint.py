#kapiska
"""
def vizszint(magassag):
    if magassag <= 200:
        return "ez alföld"
    elif 200 <= magassag <= 500:
        return "ez dombság"
    elif 500 <= magassag <= 1500:
        return "ez középhegység"
    else:
        return "ez magashegység"

hely = input("Add meg egy földrajzi hely nevét")
magassag = int(input("Add meg a tegerszint feletti magasságot méterben!"))

print(vizszint(magassag))
"""
#jó megoldás
"""
def tengerszint(szint):
    if szint < 200:
        return True
    elif szint > 200 and szint < 500:
        return False
nev = "a"
while nev:
    nev = input("Add meg a földrajzi hely nevét!")
    if nev:
        szint = int(input("Add meg a tengerszint feletti magasságát."))
        if tengerszint:
            print(f"{nev} egy alföld")
        else:
            print(f"{nev} egy dombság")
"""
#legjobb megoldás
def tengerszint(szint):
    if szint < 200:
        return "alföld"
    elif szint >= 200 and szint < 500:
        return "dombság"
    elif szint >= 500 and szint < 1500:
        return "középhegység"
    else:
        return "magashegység"

nev = "a"
while nev:
    nev = input("Add meg a földrajzi hely nevét!")
    if nev:
        szint = int(input("Add meg a tengerszint feletti magasságát!"))
        print(f"{nev} egy {tengerszint(szint)}")