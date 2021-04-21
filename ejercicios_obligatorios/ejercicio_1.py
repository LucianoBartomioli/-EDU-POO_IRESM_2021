
def cargar_funcion():
    cantidad_espectadores = int(input("Ingrese la cantidad de espectadores: "))
    descuento = str(input("Ingrese si la funcion sera con descuento (SI/NO): "))
    funcion = [cantidad_espectadores, descuento]
    return funcion


def calcular_recaudacion_total(funciones):
    cantidad_de_funciones = len(funciones)
    total_recaudado = 0
    cantidad_funciones_descuento = 0
    cantidad_funciones_sin_descuento = 0
    for funcion in funciones:
        cantidad_espectadores = funcion[0]
        descuento_aplicado = funcion[1]
        if descuento_aplicado == "si":
            cantidad_funciones_descuento = cantidad_funciones_descuento + 1
            precio_funcion_descuento = 50
            total_recaudado_por_funcion = cantidad_espectadores * precio_funcion_descuento
        else:
            total_recaudado_por_funcion = cantidad_espectadores * 75
        total_recaudado = total_recaudado + total_recaudado_por_funcion
    return [cantidad_funciones_descuento, total_recaudado]


def opcion_menu():
    opcion = int(input("""
    ---------------MENU-----------
    (1) CARGAR FUNCION
    (2) CALCULAR RECAUDACION TOTAL
    (3) FUNCIONES CON DESCUENTO
    (0) PARA SALIR

    Ingrese una opcion: """))
    return opcion

# La carga finaliza cuando se selecciona otra opcion en el menu.
funciones = []
opcion_menu_ = opcion_menu()
while opcion_menu_ != 0:


    if opcion_menu_ == 1:
        nueva_funcion = cargar_funcion()
        funciones.append(nueva_funcion)
    elif opcion_menu_ == 2:
        total_recaudado = calcular_recaudacion_total(funciones)[1]
        print(f"El total recaudado es ${total_recaudado}")
    elif opcion_menu_ == 3:
        cantidad_funciones_descuento = calcular_recaudacion_total(funciones)[0]
        porcentaje_funciones_descuento = cantidad_funciones_descuento * 100 / len(funciones)
        print(f"Se realizaron {cantidad_funciones_descuento} funciones con descuento, que representan el {porcentaje_funciones_descuento}% del total de funciones")
    opcion_menu_ = opcion_menu()
















