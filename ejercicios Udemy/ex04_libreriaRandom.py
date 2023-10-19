# Ejercicios lección 4 - LIBRERIA RANDOM

#para importar todos los métodos al mismo tiempo:
from random import *

# Desde la librería random importamos el método randint
# Randint perdite generar números aleatorios
from random import randint
numero_aleatorio = randint(0,100)
print(numero_aleatorio)

# uniform() importa un nº decimal aleatorio
from random import uniform
numero_aleatorio = uniform(0,100)
print(numero_aleatorio)

numero_aleatorio = round(uniform(0,100),2) #redondeamos para tener sólo 2 decimales
print(numero_aleatorio)

# random() importa un nº aleatotio entre 0 y 1
from random import random
numero_aleatorio = random()
print(numero_aleatorio)

numero_aleatorio = round(random(),2) #redondeamos para tener sólo 2 decimales
print(numero_aleatorio)

# Choice() selecciona aleatoriamente de una lista que le demos:
colores = ['rojo','verde','azul','naranja','negro']
color_aleatorio = choice(colores)
print(color_aleatorio)

# Shuffle() mezcla el contenido de una lista que le demos.
# No puede usarse con strings al ser inmnutables.
numeros = list(range(0,51,5))
print(numeros)
shuffle(numeros)
print(numeros)