import random


opcion_menu = int(input("""
-----------------MENU---------------
(1) Calcular suma de cuadrados
(2) Determinar cantidad de palabras que finalizan con vocales en un texto 
(3) Determinar mayor cantidad de pares e impares
(0) Salir
INGRESE SU OPCION: 
"""))

if opcion_menu == 1:
    numeros_generados = []
    cantidad_numeros = int(input("Ingrese la cantidad de numeros que desea generar: "))
    for numero in range(0, cantidad_numeros):
        numero = random.randrange(100)
        numeros_generados.append(numero)


    numero_al_cuadrado = 0

    for numero_ in numeros_generados:
        numero_al_cuadrado = numero_al_cuadrado + numero_**2
    print(f"Los numeros generados son {numeros_generados}")

    print(f"La suma de los cuadrados es igual a {numero_al_cuadrado}")

if opcion_menu == 2:
    texto = input(str("Ingrese un texto finalizado por un punto: "))
    cantidad_palabras_terminadas_en_vocal = 0
    letra_anterior = ""
    for letra in texto:
        if letra == " ":
            if letra_anterior == "a":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "e":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "i":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "o":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "u":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
        if letra == ".":
            if letra_anterior == "a":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "e":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "i":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "o":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1
            elif letra_anterior == "u":
                cantidad_palabras_terminadas_en_vocal = cantidad_palabras_terminadas_en_vocal + 1

        letra_anterior = letra
    print(f"Son {cantidad_palabras_terminadas_en_vocal} las palabras terminadas con vocal.")

if opcion_menu == 3:
    numeros_ingresados_lista = []
    numeros_ingresados = 1
    numeros_pares = 0
    numeros_impares = 0
    while numeros_ingresados != 0:
        numeros_ingresados = int(input("Ingrese un numero: "))
        if numeros_ingresados != 0:

            numeros_ingresados_lista.append(numeros_ingresados)
    for numero__ in numeros_ingresados_lista:
        resultado_division = numero__ % 2
        if resultado_division == 0:
            numeros_pares = numeros_pares + 1

        else:
            numeros_impares = numeros_impares + 1

    if numeros_impares > numeros_pares:
        print("Hay mayor cantidad de numeros impares")
    elif numeros_impares == numeros_pares:
        print("Hay la misma cantidad de numeros pares que impares")
    else:
        print("Hay mayor cantidad de numeros pares")





