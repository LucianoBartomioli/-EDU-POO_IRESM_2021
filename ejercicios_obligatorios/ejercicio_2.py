
nombre_ciclista = ""
ciclistas = []
while nombre_ciclista != "0":

    nombre_ciclista = input("Ingrese el nombre del ciclista: ")
    if nombre_ciclista != "0":
        tiempo_de_carrera = float(input("Ingrese el tiempo de carrera: "))
        if tiempo_de_carrera < 0:
            while tiempo_de_carrera < 0:
                print("¡El tiempo de carrera no puede ser negativo!")
                tiempo_de_carrera = input("Ingrese nuevamente el tiempo de carrera: ")

        ciclista_lista = [nombre_ciclista, tiempo_de_carrera]
        ciclistas.append(ciclista_lista)

tiempo_record = int(input("Ingrese el tiempo record: "))
cantidad_ciclistas = len(ciclistas)
mejor_tiempo = 999999999
suma_tiempos = 0
for ciclista in ciclistas:
    suma_tiempos = suma_tiempos + ciclista[1]
    tiempo_ciclista = ciclista[1]
    if ciclista[1] < mejor_tiempo:
        mejor_tiempo = ciclista[1]
        ciclista_ganador = [ciclista[0], mejor_tiempo]
print()
print(f"El ciclista ganador es {ciclista_ganador[0]} con un tiempo de {ciclista_ganador[1]}")
print()
if ciclista_ganador[1]< tiempo_record:
    print(f"El ciclista {ciclista_ganador[0]} supero el tiempo record de {tiempo_record}")
elif ciclista_ganador[1]== tiempo_record:
    print(f"El ciclista {ciclista_ganador[0]} igualó el tiempo record de {tiempo_record}")
else:
    print(f"El ciclista {ciclista_ganador[0]} supero el tiempo record de {tiempo_record}")
tiempo_promedio_ciclistas = suma_tiempos / len(ciclistas)

print(f"El promedio de tiempo de carrera es {tiempo_promedio_ciclistas}")



