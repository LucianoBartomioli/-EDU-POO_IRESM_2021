num = int
numeros =  []
p = int
q = int

while num !=0:
    numeros.append(num)
    num = input("Ingrese un numero: ")

p = int(input("Ingrese el rango p: "))
q = int(input("Ingrese el rango q: "))
while p <= 0 and q <= 0:
    p = int(input("Ingrese el rango p: "))
    q = int(input("Ingrese el rango q: "))
p1 = 0
q1 = 0
if q > p:
    q = p1
    p = q1
    p1 = p
    q1 = q
numeros_entre_rango = []
for numero in numeros:
    if numero > q and numero < p:
        numeros_entre_rango.append(numero)

contador_num_cont = 0
num_anterior = 1

for numero in numeros:

    det_par = int(numero % 2)
    det_par_ant = int(num_anterior % 2)
    if det_par == 0 and det_par_ant == 0 :

        contador_num_cont = contador_num_cont + 1
    num_anterior = int(numero)

primer_num_secuencia = numeros[0]
cont_num_multiplos = 0
cont = 0
for numero in numeros:
    resto = numero % primer_num_secuencia
    if resto == 0 and cont != 0:
            cont_num_multiplos = cont_num_multiplos + 1
    cont = cont + 1
acum = 0
cont2 = 0
for numero in numeros:
    if cont2 != 0:
        acum = acum + numero
    cont2 = cont2 + 1

porcentaje_primer_num = numeros[0] * 100 / acum


print(f"La cantidad de numeros en el rango p y q son: {len(numeros_entre_rango)}")
print(f"La cantidad de numeros contiguos pares son: {contador_num_cont}")
print(f"La cantidad de numeros que son multiplos del primero son: {cont_num_multiplos}")
print(f"El primer numero representa el %{porcentaje_primer_num} del total de la secuencia.")







