#Resolucion TP Estructuras Repetitivas

# Ejercicio 1
i = 0

for i in range (0, 101):
    print(i)

# Ejercicio 2

numero = int(input("ingrese un numero: "))
# str lo convierte en cadena 

# len cuenta cuántos caracteres tiene esa cadena
cantidad_digitos = len(str(numero))

print("El numero tiene", cantidad_digitos, "digitos")

# Ejercicio 3

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

# Asegurar que a sea el menor y b el mayor
menor = min(numero1, numero2)
mayor = max(numero2, numero1)

suma = 0
for i in range(menor + 1, mayor ):
    suma += i

print("La suma de los numeros entre", menor, "y", mayor, "es:", suma)

# Ejercicio 4
contador = 0
numero = None #la inicio asi ya que tiene que ser != 0

while numero !=0:
    numero = int(input("Ingrese un numero (0 para terminar): "))
    contador += numero

print("El total acumulado es:", contador)

# Ejercicio 5

import random
contador = 0

numero = random.randint(0, 9)

while True:
    intento = int(input("Adivina el numero entre 0 y 9: "))
    contador += 1
    if intento == numero:
        print(f"Felicidades! Adivinaste el numero {numero} en {contador} intentos.")
        break
    else:
        print("Intenta de nuevo.")

# Ejercicio 6

numero = 100
for i in range (numero, 0 -2 , -2):
    print(i)

# Ejercicio 7
num = int(input("ingrese un numero positivo : "))

if num < 0:
    print("El numero es negativo, pruebe con un numero positivo")
else:  
    suma = 0
    for i in range(1, num):
        suma += i

    print("La suma de los numeros entre 1 y", num, "es:", suma)

# Ejercicio 8
cantidad = 100
numPar = 0
numImpar = 0
positivos = 0
negativos = 0

for i in range(0, cantidad):
    numero = int(input(f"Ingrese {cantidad} numeros: "))
    
    if numero % 2 == 0:
        numPar += 1
    else:
        numImpar += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {numPar}")
print(f"Impares: {numImpar}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# Ejercicio 9

cantidad = 100
media = 0
suma = 0
for i in range(0, cantidad):
    numero = int(input(f"Ingrese {cantidad} numeros: "))
    suma += numero
    
media = suma / cantidad
print(f"La media de los numeros ingresados es: {media}")

# Ejercicio 10

numero = int(input("Ingrese un número entero: "))
invertido = 0

while numero != 0:
    digito = numero % 10        # Tomar el último dígito
    invertido = invertido * 10 + digito  # Agregarlo al número invertido
    numero = numero // 10       # Quitar el último dígito al original

print(f"El número invertido es: {invertido}")

