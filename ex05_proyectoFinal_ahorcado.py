# Proyecto Final lección 5 - Juego "Ahorcado"

import random

def elegir_palabra(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra
lista_palabras = ["python", "programacion", "ordenador", "teclado", "raton"]
palabra_secreta = elegir_palabra(lista_palabras)
print(palabra_secreta)

def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada
letras_adivinadas = ["o", "r", "n", "a"]
palabra_mostrada = mostrar_palabra(palabra_secreta, letras_adivinadas)
print(palabra_mostrada)

def pedir_letra():
    letra = input("Ingresa una letra: ")
    while not letra.isalpha():
        letra = input("Ingresa una letra válida: ")
    return letra.lower()
letra_ingresada = pedir_letra()
print(letra_ingresada)

def verificar_letra(letra, palabra, letras_adivinadas):
    if letra in palabra and letra not in letras_adivinadas:
        return True
    else:
        return False
letra = "o"
letras_adivinadas = ["o", "r", "n", "a"]
es_letra_valida = verificar_letra(letra, palabra_secreta, letras_adivinadas)
print(es_letra_valida)

def verificar_letra(letra, palabra, letras_adivinadas):
    if letra in palabra and letra not in letras_adivinadas:
        return True
    else:
        return False
letra = "o"
letras_adivinadas = ["o", "r", "n", "a"]
es_letra_valida = verificar_letra(letra, palabra_secreta, letras_adivinadas)
print(es_letra_valida)

lista_palabras = ["python", "programacion", "ordenador", "teclado", "raton"]
palabra_secreta = random.choice(lista_palabras)
jugar(palabra_secreta)

# Para que se elijan palabras al azar sin tener que meterlas:
# 1º Crear base de datos en archivo de texto con las palabras (cada una en una línea).
# 2º Lee el archivo de texto y almacena todas las palabras en una lista.
# 3º Utilizar la función  random.choice()  para seleccionar una palabra aleatoria de la lista.
# Ejemplo:
'''
import random
 def obtener_palabra_aleatoria():
    with open("base_de_datos.txt", "r") as archivo:
        palabras = archivo.readlines()
     palabra_secreta = random.choice(palabras).strip()
    return palabra_secreta
 palabra_secreta = obtener_palabra_aleatoria()
jugar(palabra_secreta)
'''