import time

def visszaszámlálás(t):
	
	while t:
		mins, secs = divmod(t, 60)
		visszaszámláló = '{:02d}:{:02d}'.format(mins, secs)
		print(visszaszámláló, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Kilövés!!!')

t = input("Írd be hány óra múlva legyen a kilövés: ")
#Egy másodperc valóságban az itt egy óra
visszaszámlálás(int(t))
