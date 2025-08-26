#adjunto el trabajo finalizado

#1
print("Hola Mundo.!")

#2
nombre = input("diga su nombre por favor: ")
print(f"Hola {nombre}!")

#3
nombre=input("diga su nombre: ")
apellido=input("apellido: ")
residencia=input("lugar donde reside: ")
edad=int(input("diga su edad"))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
radio=int(input("diga el radio del circulo "))
diametro = radio*2
Pi=3.1415
print(f"el perimetro del circulo es: ",diametro*Pi)
print(f"y su area es: ",Pi*(radio*radio))

#5
seg=int(input("diga los segundos quiere pasar a horas: "))
horas= seg/60
print(seg,f"equivale a ,{horas} horas")

#6
numero = int(input("diga un numero: "))
print(numero*1,numero*2,numero*3,numero*4,numero*5,numero*6,numero*7,numero*8,numero*9,numero*10)

#7
numero1=int(input("diga su numero mayora 0: "))
numero1 > 0
numero2=int(input("diga un segundo numero mayor a 0: "))
numero2 > 0

suma = numero2 + numero1
resta= numero1 - numero2
mult = numero2 * numero1
div  = numero1 / numero2

print(f"la suma entre las variables dadas son:{suma} ,la resta:{resta}, la multiplicacion:{mult}, y division:{div} ")

#8
altura= float(input("diga su altura en M: "))
peso  = float(input("diga su peso en Kg: "))
IMC = peso/(altura*altura)

print(f"su indice de masa corporal es: {IMC}")

#9
Celcius = float(input("diga la temperatura en celcius que quiera conocer en farenheit: "))
equivalencia = (Celcius * 9/5) + 32
print(f"el equivalente de {Celcius}C° a farenheit es: {equivalencia}°F")

#10
n1 =int(input("diga un numero: "))
n2 =int(input("diga un numero: "))
n3 =int(input("diga un numero: "))
promedio = (n1 + n2 + n3)/3

print(f"el promedio de los 3 numeros ingresados es : {promedio}")