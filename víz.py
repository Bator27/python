from pickletools import read_uint1


class Víz:
    def __init__(self, halmazállapot, hőm):
        self.halmazállapot = halmazállapot
        self.hőm = hőm
    def folyadék(halmazállapot):
        if halmazállapot == "folyékony":
            return "Víz"
        elif halmazállapot == "szilárd":
            return "jég"
        else:
            return "Gőz"
    def hőmésréklet(hőm):
        if hőm >= 100:
            return "forró"
        elif 100 > hőm > 50:
            return "meleg"
        else:
            return "fagyos"
halmazállapot = input("Adja meg a víz halmazállapotát!")
while hőm:
    hőm = int(input("Hány fokos?"))
    viz = Víz
    halmazállapot.append(Víz)
    print(viz)
"""
for x in halmazállapot:
    print()
"""
#nem működik
