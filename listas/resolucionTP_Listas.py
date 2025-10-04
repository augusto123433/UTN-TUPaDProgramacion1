#actividad 1
notas=[14,23,45,23,12,34,56,78,90,49]
print(notas)
#mapeo de notas y voy usando "suma" como contador
for nota in notas:
    suma=0
for nota in notas:
    suma+=nota
print("El promedio es:",suma/len(notas))
#buscar la nota mas alta y la mas baja
nota_alta=0
nota_baja=0
for nota in notas:
    if nota>nota_alta:
     nota_alta=nota
else:
       nota_baja=nota
print("La nota mas alta es:",nota_alta)
print("La nota mas baja es:",nota_baja)

#actividad 2
lista=[]
for i in range(5):
    producto=input("Ingrese un producto:")
    lista.append(producto)
sorted(lista)
print(lista)
#eliminar un elemento de la lista: le pido el nombre del producto "n" y si ese producto esta en la lista, lo elimino
eliminar=input("Ingrese el producto a eliminar:")
if eliminar in lista:
    lista.remove(eliminar)
    print("El producto fue eliminado")
print("La lista actual es:",lista)

#actividad 3
import random
numeros=[]
listapar=[]
listaimpar=[]
for i in range(15):
    numero=random.randint(1,100)
    numeros.append(numero)

    if numero%2==0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
print(listapar)
print(listaimpar)

#actividad 4
Datos= [1, 3, 5, 3, 7, 1, 9, 5, 3]
nuevos_Datos= []
for dato in Datos:
    nuevos_Datos.append(dato)
    if dato == dato:
        Datos.remove(dato)
print("Datos sin repeticiones:",nuevos_Datos)

#actividad 5
alumnos=["alejo", "alan", "andres", "carla", "dario", "emma", "gaby", "mariana"]
print("digite 1 si quiere eliminar a un alumno")
print("digite 2 si quiere agregar un alumno nuevo")
opcion=int(input("ingrese la opcion:"))
if opcion==1:
    eliminar=input("ingrese el nombre del alumno a eliminar:")
    if eliminar in alumnos:
        alumnos.remove(eliminar)
        print("el alumno fue eliminado")
    else:
        print("el alumno no se encuentra en la lista")
elif opcion==2:
    agregar=input("ingrese el nombre del alumno a agregar:")
    alumnos.append(agregar)
    print("el alumno fue agregado")

print("la lista actual es:",alumnos)

#actividad 6

numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:", numeros)

# Rotar una posición a la derecha usando slicing (rebanado)
#creamos una lista qeu contiene el ultimo numero de la lista numeros y se concatena con "+" con la lista numeros sin su ultimo elemento ":-1"
numeros = [numeros[-1]] + numeros[:-1]

print("Lista rotada:", numeros)

#actividad 7
temperaturas = [
    [12, 23],
    [10, 20],
    [8, 25],
    [14, 24],
    [13, 26],
    [9,  21],
    [10, 22] 
]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(temperaturas)):
 print(f"{dias[i]}  Mín: {temperaturas[i][0]}°C  ||   Máx: {temperaturas[i][1]}°C")
 
 #calculamos promedio

suma_min = 0
suma_max = 0

for temp in range(len(temperaturas)):
    suma_min += temperaturas[temp][0]
    suma_max += temperaturas[temp][1]

print("El promedio de las temperaturas mínimas es:", suma_min / len(temperaturas))
print("El promedio de las temperaturas máximas es:", suma_max / len(temperaturas))

#mayor amplitud
mayor_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

print("El día con mayor amplitud térmica es:", dia_mayor_amplitud, "con una amplitud de", mayor_amplitud, "°C")

#actividad 8
notas_estudiantes = [[7, 6, 8],
                     [9, 8, 7],
                     [6, 7, 8],
                     [8, 9, 10],
                     [1, 4, 7]]

estudiantes=["abril", "gonzalo", "lucrecia", "jazmin", "marcos"]
materia = ["matematica", "programacion", "ciencias"]

for i in range(len(notas_estudiantes)):
    suma = 0
    for j in range(len(notas_estudiantes[i])):
        suma += notas_estudiantes[i][j]
    promedio = suma / len(notas_estudiantes[i])
    print(f"El promedio de {estudiantes[i]} es: {promedio}")

print()

for j in range(len(materia)):
    suma = 0
    for i in range(len(notas_estudiantes)):
        suma += notas_estudiantes[i][j]
    promedio = suma / len(notas_estudiantes)
    print(f"El promedio de {materia[j]} es: {promedio}") 

#actividad 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero():
    print("\nTablero actual:")
    for fila in tablero:
        print(" ".join(fila))  # une los elementos de la fila con espacios

# --- Juego principal ---
jugadores = ["X", "O"]

print("🎮 Bienvenido al Ta-Te-Ti")
mostrar_tablero()

for turno in range(9):
    jugador = jugadores[turno % 2]  # alterna entre X y O
    print(f"\nTurno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0, 1 o 2): "))
    columna = int(input("Ingrese la columna (0, 1 o 2): "))

    # Validar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada. Perdés el turno.")
        continue
#refrescamos el tablero
    mostrar_tablero()

#actividad 10

# Matriz 4x7: 
ventas = [
    [10, 12, 8, 14, 11, 9, 10],
    [7, 9, 11, 10, 13, 8, 9], 
    [12, 15, 14, 13, 16, 17, 18],
    [5, 6, 8, 7, 5, 6, 8]
]

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

# Mostrar matriz
print("Ventas de la semana (productos x días):\n")
for i in range(len(ventas)):
    print(f"Producto {i+1}: {ventas[i]}")

# Total vendido por cada producto
print(" Total vendido por cada producto:")
for i in range(len(ventas)):
    total_producto = 0
    for j in range(len(ventas[i])):
        total_producto += ventas[i][j]
    print(f"Producto {i+1}: {total_producto} unidades")

# Día con mayores ventas totales
print(" Día con mayores ventas totales:")
mayor_total = 0
dia_mayor = ""
for j in range(len(dias)):
    total_dia = 0
    for i in range(len(ventas)):
        total_dia += ventas[i][j]
    print(f"{dias[j]}: {total_dia} unidades vendidas")
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = dias[j]

print(f"El día con más ventas fue el {dia_mayor} ({mayor_total} unidades)")

# 3 Producto más vendido en toda la semana
mayor_producto = 0
producto_mayor = 0

for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    if total_producto > mayor_producto:
        mayor_producto = total_producto
        producto_mayor = i + 1

print(f"El producto más vendido fue el Producto {producto_mayor} con {mayor_producto} unidades.")
