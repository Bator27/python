#1
"""
import math
magassag = int(input("Kérem adja meg magasságát!"))
suly = int(input("Kérem adja meg a testsúlyát!"))
bmi = suly/magassag2
magassag2 = magassag1*2
magassag1 = magassag/100
if bmi <= 16:
    print("Ön súlyosan alultáplált!")
elif bmi <= 18.5:
    print("Ön alultáplált!")
elif bmi <= 25:
    print("Ön egészséges!")
elif bmi <= 30:
    print("Ön túlsúlyos!")
else:
    print("Ön nagyon túl súlyos!")
#else:("Érvényes adatok megadását kérem!")
"""
#2
"""
magassag = float(input("Adja meg a magasságát cm-ben"))
suly = float(input("Adja meg a súlyát!"))

def szamol():
    magassag = magassag/100
    bmi=suly/(magassag*magassag)
    return bmi

def bmi():
    if(bmi>0):
        if (bmi<=16):
            return "Ön súlyosan alultáplált!"
        elif (bmi<=18.5):
            return "Ön alultáplált!"
        elif(bmi<=25):
            return "Ön egészséges!"
        elif(bmi<=30):
            return "Ön túlsúlyos!"
        else:
            return "Ön nagyon túlsúlyos!"
    else:
        ("Érvényes adatok megadását kérem!")
bmi()
print("A maga testsúly indexe: ", szamol(magassag, suly))
"""
#3
class Ember:
    def __init__(self, nev, magassag, suly):
        self.nev = nev
        self.magassag = magassag
        self.suly = suly
    
    def szamol(magassag, suly):
        magassag = magassag/100
        bmi= suly/(magassag*magassag)
        return bmi

    def bmi():
    if(bmi>0):
        if (bmi<=16):
            return "Ön súlyosan alultáplált!"
        elif (bmi<=18.5):
            return "Ön alultáplált!"
        elif(bmi<=25):
            return "Ön egészséges!"
        elif(bmi<=30):
            return "Ön túlsúlyos!"
        else:
            return "Ön nagyon túlsúlyos!"
    else:
        ("Érvényes adatok megadását kérem!")
bmi()
print("A maga testsúly indexe: ", szamol(magassag, suly))
nev = input("Kérem adja meg a nevét!")
magassag = int(input("Kérem adja meg magasságát!"))
suly = int(input("Kérem adja meg a testsúlyát!"))