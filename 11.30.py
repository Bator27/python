
lista = [1,2,3,4,5,"abc","def"]
with open('Dávid2.txt', 'w') as file:
    for item in lista:
        file.write("%s\n" % item)

f = open("Dávid2.txt")
tartalom = f.read()
print(tartalom)
f.close()
