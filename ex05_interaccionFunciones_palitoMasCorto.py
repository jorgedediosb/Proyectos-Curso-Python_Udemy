# Ejercicios lección 5 - INTERACCIÓN FUNCIONES

# JUEGO SACAR EL PALITO MÁS CORTO

# Importamos la función shuffle que permite mexclar elementos
from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Función para mezclar los palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista

# Función pedir intento al jugador
def probar_suerte():
    intento = ''
    # Pedimos que elija un nº
    # Si el nº está mal escrito o está fuera del rango (1,4) vuelve a pedirlo
    while intento not in ['1','2','3','4']:
        intento = input('Elige un nº del 1 al 4: ')
    return int(intento)

# Función para comprobar el intento del jugador
def comprobar_intento(lista,intento):
    if lista[intento - 1] == '-':
        #debemos restar 1 a la lista porque las listas empiezan con 0 y la lista del juego empieza en 1
        print("¡Acertáste! Sacaste el palito más corto")
    else:
        print("¡Fallaste!")
    print(f"El palito con suerte era el: {lista[intento-1]}")

# Invocación funciones / Interacción funciones
palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados,seleccion)