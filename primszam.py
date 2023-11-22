def prim1(x:int):
    if x <= 1:
        print("Nem primszam")
    elif x == 2:
        print("A 2 primszam")
    else:
        oszto_db = 0
        for i in range(3,x-1,1):
            if (x%i==0):
                oszto_db += 1
        
        if oszto_db==0:
            print(f"{x} prím")
        else:
            print(f"{x} nem prím")
    


    