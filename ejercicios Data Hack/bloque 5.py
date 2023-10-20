# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 18. Adivina el número entre 1 y 100.
from random import randint

print('EJERCICIO 18 "ADIVINA EL Nº"')

#función que genera el número aleatorio con corrección por si min > max:
def generaNumeroAleatorio(min, max):
    if min > max:
        aux = min
        min = max
        max = aux
    return randint(min, max)

numero_buscado = generaNumeroAleatorio(1, 100)
encontrado = False
intentos = 0
#Mientras 'encontrado' sea Falso (no lo hayamos encontrado):
while not encontrado:
    try:
        numero_jugador = int(input('Adivina el número que estoy pensando: '))
    #Excepción por si no se escribe un dígito:
    except ValueError:
        print('¡Debes escribir un número!')
        continue
    if numero_jugador < numero_buscado:
        print('¡Incorrecto! El número es MAYOR')
        intentos +=1
        if intentos == 1:
            print(f'LLevas {intentos} intento.')
        else:
            print(f'LLevas {intentos} intentos.')
    elif numero_jugador > numero_buscado:
        print('¡Incorrecto! El número es MENOR')
        intentos += 1
        if intentos == 1:
            print(f'LLevas {intentos} intento.')
        else:
            print(f'LLevas {intentos} intentos.')
    else:
        encontrado = True
        print(f'¡ACERTASTE! El número era {numero_buscado}')
        print(f'Has adivinado el número en {intentos} intentos.')
