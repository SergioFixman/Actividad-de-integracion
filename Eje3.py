texto = "Hoy no voy a dormir en el dormitorio porque hace mucho calor en el cuarto del cuarto" 

# Los caracteres que no contamos como palabras
quitar = ",;:.\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter,
                          "")  # Remplazarlo por "nada"; es decir, removerlo
# Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
texto = texto.lower()
# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = texto.split(" ")
# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")