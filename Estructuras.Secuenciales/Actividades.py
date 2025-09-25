    # actividad 1
edad = int(input("ingrese su edad :"))
if edad> 18 :
    print("usted es mayor de edad")
    
    # actividad 2
    nota=int(input("inserte su nota: "))
if nota>=6 :
    print("Aprobado")
else:
    print("Desaprobado")

    # actividad 3
num=int(input("ingrese un numero: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    # actividad 4
edad=int(input("ingrese su edad: "))
if edad<12:
    print("niño")
elif edad>=12 and edad<18:
    print("adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")
else:
    print("adulto/a")
    # actividad 5
contraseña=len(input("Ingrese una contraseña: "))
if contraseña>=8 and contraseña<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    # actividad 6
import random 
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
if mean(numeros_aleatorios)>median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print("Sesgo positivo")
elif mean(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print("Sesgo negativo")
elif mean(numeros_aleatorios)==median(numeros_aleatorios) and median(numeros_aleatorios)==mode(numeros_aleatorios):
    print("Sin sesgo")

    #actividad 7
palabra=input("diga una frase/palabra :")
if palabra[-1] == "a" or palabra[-1] == "e" or palabra[-1] == "i" or palabra[-1] == "o" or palabra[-1] == "u":
	print(palabra + "!")
else:
	print(palabra)

#actividad 8:
nombre = input("Diga su nombre: ")

print("Digite:")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")

numero = int(input("Ingrese su opción: "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Opción no válida")

#actividad 9

magnitud=float(input("digite la magnitud del terremoto según la escala de Richter"))

if  magnitud < 3:
	print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
	print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud <5:
	print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud <6:
	print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud <7:
	print("Muy Fuerte (puede causar daños significativos)")
else:
	print("Extremo (puede causar graves daños a gran escala)")

# actividad 10

hemisferio = input("¿En qué hemisferio está? (N/S): ")
mes = int(input("Diga el mes actual (1-12): "))
dia = int(input("Diga el día (1-31): "))
hemisferio = hemisferio.upper()

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
        print("Estación: Invierno")
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
        print("Estación: Primavera")
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
        print("Estación: Verano")
    else:
        print("Estación: Otoño")

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
        print("Estación: Verano")
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
        print("Estación: Otoño")
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
        print("Estación: Invierno")
    else:
        print("Estación: Primavera")

else:
    print("Hemisferio no válido. Use 'N' o 'S'.")
