egyik = int(input("Addjon meg egy szamot"))
masik = int(input("Addjon meg egy masik szamot"))
jel = input("Addjon meg egy masik szamot")

#print('A müvelet eredmenye:', end='' )
print('A müvelet eredmenye:',end='' )
if jel == '+':
     print(egyik+masik)
elif jel == '-':
    print(egyik-masik)
elif jel == '%':
    print(egyik % masik)
elif jel == '/':
    print(egyik / masik)
elif jel == '>>':
    print(egyik >> masik)

