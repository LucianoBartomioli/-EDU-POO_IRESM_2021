texto = ""
texto = "hola asa dada sad asa apa SADS."
# texto = input(str("Ingrese un texto finalizado por un punto: "))
ultima_vocal_contador = 0
palabras_que_terminan_y_empiezan_vocal = 0
letra_anterior = ""
primera_letra_vocal_true = False
ultima_letra_vocal_true = False
vocales = "aeiou"
for letra in texto:
    if letra == " ":
        if texto[letra + 1] in vocales:
            primera_letra_vocal_true = True

    letra_random = letra[-1]
    print(letra_random)








print(palabras_que_terminan_y_empiezan_vocal)