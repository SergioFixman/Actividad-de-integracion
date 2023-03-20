def get_int():
    estabien=False
    a = input("Ingrese un numero: ")    
    try:
        print(int(a))
        estabien= True
    except ValueError:
        print("dije un numero!!!!!")
        get_int()
    return(a)


get_int()