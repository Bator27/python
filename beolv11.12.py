def beolvas():
    zenek=[]
    with open("playlist.csv" , "r" ,encoding = "utf-8") as file:
        sorok = file.readline()

    for sor in sorok:
        sor = sor.strip()
        darabok = sor.split(";")

        zene = {"eloado": darabok[0], "cím": darabok [1], "műfaj": darabok[2], "hossz": int(darabok[3])}
        