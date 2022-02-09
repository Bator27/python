bevételek = [1,5,2,3,4]
for bevétel in bevételek:
    összes = összes + bevétel
    print('Napi bevétel:', összes, 'picula.')
    print(f'Napi bevétel: {összes} picula.')

összes = sum(bevételek)
print('Napi bevétel:', összes, 'picula.')
bevételek = [1,5,2,3,4]
összes = 0
darab = 0
for bevétel in bevételek:
    összes+= bevétel
    darab += 1
print('Az átlagos bevétel:', összes / darab, 'picula.')