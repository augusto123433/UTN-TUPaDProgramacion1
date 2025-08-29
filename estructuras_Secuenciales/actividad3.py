#actividad 1 

edad=int(input("diga su edad: "))
if edad > 18:
    print("Es mayor de edad")

#actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#actividad 3
numPar=int(input("Ingrese un numero par: "))
if numPar%2 == 0:   
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#actividad 4
edad=int(input("diga su edad: "))
if edad < 12:
    print("Es un niño/a")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30:   
    print("Es un adulto/a joven")
else:
    print("Es un adulto/a mayor")

#actividad 5
contraseña= input("Ingrese la contraseña entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña válida")

#actividad 6
import random 
from statistics import mode, median, mean 
# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("El Sesgo es positivo")
elif moda > mediana and mediana > media:
    print("El Sesgo es negativo")
else:
    print("El Sesgo es nulo")