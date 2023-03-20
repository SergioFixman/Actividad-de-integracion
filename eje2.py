
# maximo comun divisor
# import math
def mico(a,b):

    c = min(a,b)
    d = max(a,b)
    j=2
    divi=False
    while j <= c and not divi:
        apa= int(c/j)
        apa2 = c/j
        papa= int(d/j)
        papa2 = d/j
        if apa == apa2 and papa==papa2:
           divi=True
        else:
            j=j+1
    if not divi:
        j = 0        
    return j  

a = int(input("Ingrese el primer  numero: "))
b = int(input("Ingrese el segundo numero: "))


resu=(mico(a,b))
if resu==0:
    print("Es 1 o no hay minimo comun divisor")   
else:
    print("el minimo comun divisor es ", resu)    