texto = "Hoy no voy a dormir en el dormitorio porque hace mucho calor en el cuarto del cuarto" 



def cuenta(tt):
    palabras = tt.split(" ")
    diccionario_frecuencias = {}
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1

    for palabra in diccionario_frecuencias:
        frecuencia = diccionario_frecuencias[palabra]
        #print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
    return(diccionario_frecuencias)   

def lamaxima(diccio):
    #print("esese:",diccio)
    mato=0
    lapa=""
    for palabra in diccio:
        frecuencia = diccio[palabra]
        if frecuencia > mato:
            mato= frecuencia
            lapa= palabra
    mitupla = (lapa,mato)
    return(mitupla)    


pipo="la casa de mi tia esta al lado de la casa de mi abuela tia tia tia tia"
print(lamaxima(cuenta(pipo)))
