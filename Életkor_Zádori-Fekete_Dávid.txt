f = open("eletkor.txt" , 'w')
f.write("Életkor és név:")

nev = input("Kérem adja meg a teljes nevét!")
print(nev) 

eletkor = int(input("Kérem adja meg az életkorát"))
print("Eddig ezeket a projekteket csinálta meg:")
if eletkor <= 3:
    print("Totyogónak a kettes számrendszerből")
if eletkor >= 4:
    print("Hackeljünk meg az ovodát!")
if eletkor >= 7:
    print("Felhőtechnológia a menzán")
if eletkor >= 15:
    print("Big data a középiskolában")
f.close()
