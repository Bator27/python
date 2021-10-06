év = input('Hányas évet írunk?')
print(év)
if (év %4 !=4):
    print('Ez nem egy szökő év')
elif(év %400 ==0):
    print('Ez sem szökőév')
elif(év %100 !=0):
    print('Még ez sem szökő év')
else:
    print('Ez egy szökő év')
