

def division_con_resto(a, b):

    resultado_division_entera = a//b
    resto = a % b

    print(f"Resultado de la division: {resultado_division_entera}  Resto: {resto}")


def cuadrado_de_un_binomio(a, b):

    cuadrado_de_binomio = a**2 + 2*a*b + b**2
    print(cuadrado_de_binomio)


def area_triangulo():
    base = float(input("Ingrese la base del triangulo en Cm: "))
    altura = base**2
    area = base * altura / 2

    print(f"El area del triangulo es {area}cm²")


def ultimo_digito_numero_entero():
    numero_entero = int(input("Ingrese un numero entero: "))
    ultimo_digito = numero_entero % 10
    print(f"El ultimo numero es {ultimo_digito}")
    ultimo_dos_digitos = numero_entero % 100
    print(f"Los ultimos dos numeros son: {ultimo_dos_digitos}")


def conversion_de_medidas(medida_en_pies):
    medida_en_pulgadas = medida_en_pies*12
    medida_en_yardas = medida_en_pies/3
    medida_en_centimetros = medida_en_pies * 12 / 2.54
    print(f""""
    {medida_en_pies} pies Son equivalentes a:
    {medida_en_pulgadas} Pulgadas
    {f"{medida_en_yardas:.2f}"} Yardas
    {f"{medida_en_centimetros:.2f}"} Centimetros
    """)


def viaje_cordoba_rosario():
    total_horas_viaje = 400/122

    print(f"""El viaje Cordoba-rosario tendra una demora de {f"{total_horas_viaje:.2f}"} horas """)


def precio_boleto(monto_base, kilometros_a_recorrer):
    precio_final_boleto = monto_base + (kilometros_a_recorrer*0.30)

    print(f"El precio final es ${precio_final_boleto}")


def cubos_y_cuadrados(numero1, numero2):
    suma_de_cuadrados = numero1**2 + numero2**2
    promedio_de_cubos = (numero1**3 + numero2*3)/2
    print(f"La suma de sus cuadrados es {suma_de_cuadrados} y el promedio de sus cubos es {promedio_de_cubos}")


def descuento_en_medicina():
    precio_medicamento = float(input("Ingrese el precio del medicamento: "))
    monto_final = precio_medicamento * 0.65

    print(f""""
    Pecio actual:             ${precio_medicamento}
    Porcentaje de descuento:  %35 
    Total a pagar:            ${monto_final}
    """)


def ecuacion_de_einstein():
    valor_masa_kilogramos = float(input("Ingrese el valor de masa en kilogramos: "))

    e = valor_masa_kilogramos * 299792.458 * 2
    print(f"La cantidad de energia producida es {e:.2f} ")


def polinomio_segundo_grado():                                # y = ax2 + bx + c
    a = float(input("Ingrese el valor de la pendiente: "))
    b = float(input("Ingrese el valor del b: "))
    c = float(input("Ingrese el valor de la ordenada al origen: "))
    x = float(input("Ingrese el punto en X que desea calcular: "))

    valor_en_funcion_x = a*(x**2) + b*x + c

    discriminante = b**2 - 4 * a * c

    print(f"El valor de la funcion en el punto x = {x} es: {valor_en_funcion_x}")

    print(f"El discriminante es igual a {discriminante} por lo que:")

    if discriminante > 0:
        print("La funcion tendra 2 raices")

    elif discriminante == 0:
        print("La funcion tendra 1 sola raiz")

    else:
        print("La funcion tendrá raices imaginarias")


def calculo_de_angulos():                                                   # Sistema de ecuaciones con dos incognita
    x = float(input("Ingrese el resultado de la suma de los angulos: "))
    y = float(input("Ingrese el resultado de la resta de los angulos: "))
    angulo_beta = (y - x) / -2
    angulo_alfa = x - angulo_beta

    print(f""""
    El valor de alfa es igual a {angulo_alfa}
    El valor de beta es igual a {angulo_beta}
    """)


def precio_de_venta(precio_de_lista):
    precio_venta_contado = precio_de_lista * 0.90
    precio_venta_tarjeta = precio_de_lista * 1.05
    print(f""""
    Precio Contado: ${precio_venta_contado}
    Precio Tarjeta: ${precio_venta_tarjeta}  
    """)


def votacion_en_congreso():
    votos_a_favor = int(input("Ingrese la cantidad de votos a favor: "))
    votos_en_contra = int(input("Ingrese la cantidad de votos en contra: "))

    votos_100_porciento = votos_a_favor + votos_en_contra
    porcentaje_votos_a_favor = votos_a_favor * 100 / votos_100_porciento
    porcentaje_votos_en_contra = votos_en_contra * 100 / votos_100_porciento

    print(f"El porcentaje de votos a favor es igual a {porcentaje_votos_a_favor}%")
    print(f"El porcentaje de votos en contra es igual a {porcentaje_votos_en_contra}%")


def rinde_campo_agricola():
    largo = int(input("Ingrese el largo en metros: "))
    ancho = int(input("Ingrese el ancho en metros: "))

    metros_cuadrados = largo * ancho

    quintales_obtenidos = metros_cuadrados * 2 / 10

    print(f"Quintales obtenidos {quintales_obtenidos}")


def datos_de_un_rectangulo():
    ancho = float(input("Ingrese el ancho del rectangulo en centimetros: "))
    largo = float(input("Ingrese el largo del rectangulo en centimetros: "))

    superficie = ancho * largo
    perimetro = 2*ancho + 2*largo

    print(f""""
    Superficie = {superficie} centimetros cuadrados
    Perimetro = {perimetro}
    """)


def plazo_fijo():                    # caso en un año de plazo fijo con
    dinero_depositado_en_plazo_fijo = float(input("Ingrese el dinero depositado en plazo fijo: $"))
    cont = 0
    dinero_por_mes = 0
    while cont != 12:
        dinero_plazofijo = dinero_por_mes + dinero_depositado_en_plazo_fijo
        dinero_por_mes = dinero_por_mes + dinero_plazofijo*0.023/12
        cont = cont + 1

    dinero_fin_plazo_fijo = dinero_por_mes + dinero_depositado_en_plazo_fijo

    print(f"Al finalizar el año, usted tendra ${dinero_fin_plazo_fijo:.0f}")


def fecha_con_cadena():
    fecha = str(input("Ingrese la fecha en formato dd/mm/aaaa: "))

    list(fecha)
    print(f"Día: {fecha[0:2]} - Mes: {fecha[3:5]} - Año: {fecha[6:]}")


def expresar_cantidad_dinero():
    importe = float(input("Ingrese el importe:  "))

    print(f"${importe}")
    print(f"{importe} Pesos")


""""
def duracion_de_un_vuelo(hora_partida, hora_llegada): # Si o si en formato hh:mm
    list(hora_partida)
    list(hora_llegada)
    horas_de_vuelo = (int(hora_llegada[0]*10) + int(hora_llegada[1])) - (int(hora_partida[3]*10) + int(hora_partida[4]))
    horas_de_vuelo_a_minutos = horas_de_vuelo * 60
    print(f"El vuelo duró {horas_de_vuelo_a_minutos} minutos")


duracion_de_un_vuelo("11:50", "15:30")
"""


def duracion_de_un_vuelo(hora_partida, hora_llegada): # Si o si en formato hh:mm
    list(hora_partida)
    list(hora_llegada)
    print(int(hora_llegada[0]))
    hora_partida_primerdecimal = int(hora_partida[0])
    hora_partida_segundo_decimal = int(int(hora_partida[1]))
    horas_partidas = (hora_partida_primerdecimal * 10) + hora_partida_segundo_decimal
    hora_llegada_primer_decimal = int(hora_llegada[0])
    hora_llegada_segundo_decimal = int(hora_llegada[1])
    horas_llegadas = (hora_llegada_primer_decimal * 10) + hora_llegada_segundo_decimal
    minutos_partida_primer_decimal = int(hora_partida[3])
    minutos_partida_segundo_decimal = int(hora_partida[4])
    minutos_llegada_primer_decimal = int(hora_llegada[3])
    minutos_llegada_segundo_decimal = int(hora_llegada[4])
    minutos_partida = (minutos_partida_primer_decimal*10) + minutos_partida_segundo_decimal
    minutos_llegada = (minutos_llegada_primer_decimal*10) + minutos_llegada_segundo_decimal
    total_minutos = ((horas_llegadas - horas_partidas) * 60) + (minutos_llegada - minutos_partida )

    print(f"El vuelo duró {total_minutos} minutos")

    horario_llegada_hotel = minutos_llegada + 45
    if horario_llegada_hotel > 60:
        minutos_llegada_hotel_superior_1_hora = minutos_llegada + 45 - 60
        hora_llegada_hotel_superior_1_hora = horas_llegadas + 1
        print(f"El pasajero llegara al hotel a las {hora_llegada_hotel_superior_1_hora}:{minutos_llegada_hotel_superior_1_hora}")

    else:
        print(f"El pasajero llegara al hotel a las {horas_llegadas}:{horario_llegada_hotel}")


duracion_de_un_vuelo("15:00", "18:40")


