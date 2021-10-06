#JELSZO = input('Mi a jelszava?')
#print(JELSZO)
JELSZO = 'Jelszo'
jelszo = None
while jelszo != JELSZO:
    jelszo = input('Mi a jelszava?')
    if jelszo != JELSZO:
        print('Nem jo jelszot addot meg')
        pass
print('ügyes vagy')