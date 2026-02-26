#actividad 1
def  imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo() 

#actividad 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Augusto")

#actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Augusto", "Fernandez", 28, "Córdoba")

#actividad 4
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# actividad 5 
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#actividad 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese su número para mostrar la tabla de multiplicar: "))
tabla_multiplicar(numero)

#actividad 7
def operaciones_basicas(a, b):
   suma = a + b
   resta = a - b
   multiplicacion = a * b

   if b != 0:
      division = a / b
   else:
      division = "error division por cero"

   return (suma, resta, multiplicacion, division)

resultado = operaciones_basicas(10, 5)
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")


#actividad 8


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#actividad 10

def  calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio}")
