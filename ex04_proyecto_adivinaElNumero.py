# PROYECTO LECCIÓN 4 'ADIVINA EL NÚMERO'

from random import randint

intentos = 0
numero_estimado = 0
numero_secreto = randint(0,100)
nombre = input("¿Cuál es tu nombre?: ")

print(f"""{nombre}, adivina el número secreto.
Es un número entre 0 y 100.
Tienes 8 intentos.""")

while intentos < 8:
    numero_estimado = int(input("¿Cuál es el número?: "))
    intentos += 1
    if numero_estimado < numero_secreto:
        print("¡Error! El número es mayor.")
    elif numero_estimado > numero_secreto:
        print("¡Error! El número es menor.")
    else:
        print(f"¡Correcto! {nombre} has adivinado el número en {intentos} intentos.\nEl número secreto era el {numero_secreto}.")
        break
if numero_estimado != numero_secreto:
    print(f"""Lo siento {nombre}, has agotado los 8 intentos.
El número secreto era el {numero_secreto}.
¡Vuelve a intentarlo!""")