diak = ["Oláh", "Balázs", "10/b", 16, True, False]
print(diak[3])

diak = {
"vezeteknev" : "Oláh",
"keresztnev" : "Balázs",
"osztály" : "10/b"
"eletkor" : 16,
"tanulo" : True
"info_fakt" : False
"matek_jegyek" : [5, 4, 4, 3, 5, 5]
}
print(diak["eletkor"])


raktar = {
114589: "Dominó polc",
264875: "Student iróasztal",
364879: "Kényeklem01 fotel",
568974: "Family étkezőasztal 6 fős"
}


rakter = {}
print(raktar)

diak = {
"vezeteknev" : "Oláh",
"keresztnev" : "Balázs",
"osztály" : "10/b"
"menza" : True
}
print(diak.get("szakkor", "nincs adat"))
print(szakkor in diak)

diak["szakkor"] = True
print(diak)

diak["eletkor"] = 16
print(diak)

del diak["vezeteknev"]
print(diak)

for kulcs in diak:
    print(kulcs, diak[kulcs])

print(diak.value())
for ertek in diak.values():
    print(ertek)

for kulcs, ertek in diak.items():
    print(kulcs, ertek)
