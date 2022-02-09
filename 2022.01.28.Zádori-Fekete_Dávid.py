#from re import search , avg
wr = open("zsák.txt" , 'w')
#from audioop import avg
zsák = [2, 9, 19, 20, 5]
össz = sum(zsák)
print(f'A zsák össz súlya: {össz}')
wr.write(f'A zsák össz súlya: {össz}')
"""
print("A zsák össz kilogram száma:")
print(sum(zsák))
"""
"""
print("A zsák össz és átlagos kilogramm száma:")
print(sum(f'A zsák összesen {zsák}kg'))
wr.write('A zsák összesen {zsák}kg')
"""
#print(avg(zsák))

i = [5]
for i in zsák:
    if i in zsák:
        print("Van 5kg-os zsák")
    else:
        print("Nincs 5kg-os zsák")

van = print(i)
print(f'Van-e 5kg?')
wr.write(f'\n van? {van}')

#print(search(i in zsák))
legkisebb = min(zsák)
legnagyobb = max(zsák)

print(f'\n A legkisebb a zsákban {legkisebb}')
wr.write(f'\n A legkisebb a zsákban kg: {legkisebb}')
"""
print("A legkisebb súlyú zsák:")
print(min(zsák))
print(min(f'A legkisebb súlyú zsák:{zsák}'))
wr.write(f'A legkisebb súlyú zsák:{zsák}')
"""
"""
print("Legnagyobb súlyú zsák:")
print(max(zsák))
print(max(f'A legnagyobb súlyú zsák: {zsák}'))
wr.write(f'A legnagyobb súlyú zsák: {zsák}')
"""
print(f'\n A legnagyobb a zsákban {legnagyobb}')
wr.write(f'\n A legnagyobb a zsákban kg: {legnagyobb}')
wr.close()