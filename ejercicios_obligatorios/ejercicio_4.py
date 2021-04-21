texto = ""
texto = "hola asa dada sad asa apa SADS."
#texto = input(str("Ingrese un texto finalizado por un punto: "))
ultima_vocal_contador = 0
palabras_que_terminan_y_empiezan_vocal = 0
letra_anterior = ""
primera_letra_vocal_true = False
ultima_letra_vocal_true = False
for letra in texto:

    if letra_anterior == " ":
        if letra == "a":
            ultima_vocal_contador = ultima_vocal_contador + 1
            primera_letra_vocal_true = True
        elif letra == "e":
            ultima_vocal_contador = ultima_vocal_contador + 1
            primera_letra_vocal_true = True
        elif letra == "i":
            ultima_vocal_contador = ultima_vocal_contador + 1
            primera_letra_vocal_true = True
        elif letra == "o":
            ultima_vocal_contador = ultima_vocal_contador + 1
            primera_letra_vocal_true = True
        elif letra == "u":
            ultima_vocal_contador = ultima_vocal_contador + 1
            primera_letra_vocal_true = True
        else:
            primera_letra_vocal_true = False

    if (ultima_letra_vocal_true == True) and (primera_letra_vocal_true == True):
        palabras_que_terminan_y_empiezan_vocal = palabras_que_terminan_y_empiezan_vocal + 1

    if letra == (" "):
        if letra_anterior == "a":
            ultima_vocal_contador = ultima_vocal_contador + 1
            ultima_letra_vocal_true = True
        elif letra_anterior == "e":
            ultima_vocal_contador = ultima_vocal_contador + 1
            ultima_letra_vocal_true = True
        elif letra_anterior == "i":
            ultima_vocal_contador = ultima_vocal_contador + 1
            ultima_letra_vocal_true = True
        elif letra_anterior == "o":
            ultima_vocal_contador = ultima_vocal_contador + 1
            ultima_letra_vocal_true = True
        elif letra_anterior == "u":
            ultima_vocal_contador = ultima_vocal_contador + 1
            ultima_letra_vocal_true = True

        else:
            ultima_letra_vocal_true = False

    primer_letra_texto = texto[0]

    if letra_anterior == " ":
        ultima_letra_vocal_true = False
    elif letra == " ":
        primera_letra_vocal_true = False
    letra_anterior = letra
print(palabras_que_terminan_y_empiezan_vocal)