szam1 = int(input("Adjon meg egy számot a zaciba: "))

def pozneg(szám1):
    if szam1 > 0:
        print(szam1, "pozitív")
    elif szam1 <0:
        print(szam1, "negatív")
    else:
        print("A szám nulla")

szám = None
while szám != "":
    szám = input("Kérem adjon meg egy számot!")
    if szam1 != "":
        szam1 = float(szam1)
    pozneg(szám)
    wr = open("ZFD.txt", "w")
    wr.write(" ")
    wr.close()

