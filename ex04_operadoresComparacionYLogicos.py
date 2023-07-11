#Ejercicios lección 4 - Operarores de comparación

#OPERADORES DE COMPARACIÓN
num1 = 36
num2 = 17
mi_bool = num1 >= num2
print(mi_bool)

num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2
print(mi_bool)

num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2
print(mi_bool)

#OPERADORES LÓGICOS (and, or, not)
num1 = 36 
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3
print(mi_bool)

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3
print(mi_bool)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not (palabra1 in frase) or (palabra2 in frase)
print(mi_bool)

#Adivina si el nº es mayor, menor o igual
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if num1 > num2:
    print(f"{num1} es mayor que 4{num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#¿Puedes conducir?
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    licencia = input("¿Tienes licencia de conducir? si o no: ")
    if edad >= 18 and licencia == "si":
        print("¡Puedes conducir!")
    elif edad >= 18 and licencia == "no":
        print("Tienes que sacarte la licencia para poder conducir")
else:
    print("Debes cumplir 18 años para poder sacarte la licencia")

#¿Buscas trabajo de programador python?
ingles = input("¿Hablas inglés? si o no: ")
python = input("¿Sabes programar en python? si o no: ")

if ingles == "si" and python == "si":
    print("¡Te espera un futuro lleno de éxitos!")
elif ingles == "no" and python == "si":
    print("Necesitas tener conocimientos de inglés para acceder a un puesto de trabajo.")
elif ingles == "si" and python == "no":
    print("Te recomiendo aprender Python para triunfar.")
else:
    print("Tienes un futuro complicado :(")