for x in range(2,101):
    for osztó in range(2,x/2+1):#4 nem lesz prím
        print(x,osztó)
        if(x % osztó ) ==0:
            break
    else:
        print(x,'prím')