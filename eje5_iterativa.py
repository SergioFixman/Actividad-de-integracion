def get_int():
    estabien=False
    while not estabien:
        a = input("Ingrese un numero: ")
        try:
            print(int(a))
            estabien= True
        except ValueError:
            print("dije un numero!!!!!")
    return(a)


get_int()