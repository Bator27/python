#1
bevételek = [3, 8, 10, 19.35, -6, 5.1, 9, 20]

vendégek = 0

for bevétel in bevételek:
    if bevétel > 0:
        vendégek += 1
    
print('A pincér', round(vendégek/2, 2), 'font fizetést kap.')
#2
mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

print('A mondat', len(mondat), 'szóból áll.')
#3
mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

legrövidebb_szó_hossza = 1000

for szó in mondat:
    if len(szó) < legrövidebb_szó_hossza:
        legrövidebb_szó_hossza = len(szó)
        
print('A legrövidebb szó', legrövidebb_szó_hossza, 'karakteres.')

mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

írásjelek = '.?!'

for szó in mondat:
    if szó[-1] in írásjelek:
        print('Van olyan szó ami után írásjel áll.')
        
mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

névelők = ['a', 'az', 'egy']

for szó in mondat:
    if szó in névelők:
        print('Van a mondatban névelő.')

mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

print('A mondatban a "fél" szó a' , mondat.index('fél')+1, '.helyen áll',sep='')

mondat = ['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénznem.']

van_nagy_kezdőbetűs = False
hol_van = None
for index in range(len(mondat)):
    if mondat[index][0].isupper():
        van_nagy_kezdőbetűs = True
        hol_van = index
        
if van_nagy_kezdőbetűs:
    print('A(z) ', hol_van+1,
    '. szó kezdődik nagy betűvel.', sep = '')