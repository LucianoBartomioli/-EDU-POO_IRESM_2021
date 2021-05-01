texto = str(input("Ingrese un texto con espacios entre palabras y finalizado por un punto: "))
letra_ant = ""
cantidad_letras_por_palabras_lista = []
cantidad_vocales_por_palabra_lista = []
cont_letras = 0
cantidad_palabras = 0
vocales = "aeiouAEIOU"
cantidad_palabras_3ra_letra_vocal = 0
cantidad_vocales_por_palabra = 0
cantidad_palabras_silaba_pe = 0
total_letras = 0
cantidad_palabras_con_1o2_vocales = 0
cant_palabras_con_357 = 0
bandera_silaba_pe = True
cantidad_palabras_2omas_silabas_pe = 0
for letra in texto:
    total_letras = total_letras + 1
    cont_letras = cont_letras + 1
    if letra in vocales and letra != " " and letra != ".":
        cantidad_vocales_por_palabra = cantidad_vocales_por_palabra + 1

    if letra_ant == "p" and letra == "e" and bandera_silaba_pe == True:
        cantidad_palabras_silaba_pe = cantidad_palabras_silaba_pe + 1

    if cantidad_palabras_silaba_pe == 2 or cantidad_palabras_silaba_pe > 2:
        cantidad_palabras_2omas_silabas_pe = cantidad_palabras_2omas_silabas_pe + 1
        bandera_silaba_pe = False
        cantidad_palabras_silaba_pe = 0
    if letra == " " or letra == ".":
        cantidad_palabras = cantidad_palabras + 1
        cantidad_letras_por_palabra = cont_letras - 1
        cantidad_letras_por_palabras_lista.append(cantidad_letras_por_palabra)
        cantidad_vocales_por_palabra_lista.append(cantidad_vocales_por_palabra)
        cantidad_vocales_por_palabra = 0
        cont_letras = 0

        bandera_silaba_pe = True
    elif cont_letras == 4:
        if letra_ant in vocales:
            cantidad_palabras_3ra_letra_vocal = cantidad_palabras_3ra_letra_vocal + 1
    letra_ant = letra
for numero in cantidad_letras_por_palabras_lista:
    if numero == 3 or numero == 5 or numero == 7:
        cant_palabras_con_357 = cant_palabras_con_357 + 1
for numero in cantidad_vocales_por_palabra_lista:
    if numero == 2 or numero == 1:
        cantidad_palabras_con_1o2_vocales = cantidad_palabras_con_1o2_vocales + 1
porcentaje_vocal_en_total = cantidad_palabras_con_1o2_vocales * 100 / cantidad_palabras

print(f"La cantidad de palabras con 3, 5 o 7 letras de longitud son: {cant_palabras_con_357}")
print(f"La cantidad de palabras con mas de 3 letras y una vocal en la tercer letrac son: {cantidad_palabras_3ra_letra_vocal}")
print(f"El porcentaje de palabras con 2 vocales sobre el total del texto es: {porcentaje_vocal_en_total:.2f}% ")
print(f"La cantidad de palabras con mas de una sílaba 'pe' es: {cantidad_palabras_2omas_silabas_pe}")
