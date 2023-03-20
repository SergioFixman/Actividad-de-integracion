
# maximo comun divisor
import math
def mcd(a,b):


    c = min(a,b)
    d = max(a,b)
    j=c
    divi=False
    while j > 1 and not divi:
        apa= int(d/j)
        apa2 = d/j
        papa= int(c/j)
        papa2 = c/j
        if apa == apa2 and papa==papa2:
           divi=True
        else:
            j=j-1
    return j  

a = int(raw_input("Ingrese el primer  numero: "))
b = int(raw_input("Ingrese el segundo numero: "))

print(mcd(a,b))