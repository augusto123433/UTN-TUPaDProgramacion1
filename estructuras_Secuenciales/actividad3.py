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