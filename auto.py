class Híres_auto:
    def __init__(self,név, henger_térfogat , nemzet):
        self.név = név
        self.henger_térfogat = henger_térfogat 
        self.nemzet = nemzet
    def nemzetiség(self):
        if self.nemzet.lower() == "j":
            return "Japán"
        elif self.nemzet.lower() == "n":
            return "Német"

autok = []

for _ in range(3):
    nev = input("Adja meg az autó márkanevét!")
    henger = int(input("Adja meg a henger térfogatát!"))
    nemzet = int(input("Adja meg az gyártó országát!"))
    auto1 = Híres_auto(nev , henger, nemzet)
    autok.append(auto1)

for auto in autok:
    print(f"{auto.név} egy {auto.nemzetiség} autó {auto.henger_térfogat} m3 henger térfogattal")
