OLVADÁSI_PONT = 1539
FORRÁSI_PONT = 2750

hőfok = int(input("Hőfok:"))

if hőfok < OLVADÁSI_PONT:
    print("Szilárd")
elif hőfok < FORRÁSI_PONT:
    print("Folyákony")
else:
    print("Gáz")
    