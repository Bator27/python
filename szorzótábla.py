print('     ', end='')
for fejléc in range (1, 11):
    print(f'  {fejléc:>3} ', end='')
print()
for szorzandó in range (1, 11):
    print(f' {szorzandó:>3}', end= '')
    for szorzó in range(1, 11):
        pass #
    print(f' {szorzó*szorzandó:>4}' , end='')
    print()