forrásfájl = open("raspberries.txt" , Encoding = "utf-8")
rpik = []
for sor in forrásfájl:
    rpik.append(sor.strip().split(';'))
forrásfájl.close()