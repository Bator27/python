import random 
egyik = random.randint(1,10)
másik = random.randint(1,10)
összeg = egyik+másik
print ('összeg')
if összeg%2 ==0:
    print('Páros')
else:
    print('Páratlan')
if összeg%3 ==0:
    print('Osztható 3-al')
else:
    print('Nem osztható 3-al')
