# PROYECTO "BUSCADOR DE ARCHIVOS"
'''
El programa busca un archivo de un directorio
'''

import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = '\\Users\\jorge\\PERSONAL\\iCode\\PROYECTOS\\Proyectos_Python\\proyectos\\p09_buscadorArchivos\\archivos'

mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()


archivos_encontrados = []
numeros_encontrados = 0

def buscar_numero(archivo, patron):
    with open(archivo, 'r') as este_archivo:
        texto = este_archivo.read()
        resultado = re.search(patron, texto)
        if resultado:
            return resultado.group()
        else:
            return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado:
                numeros_encontrados += 1
                archivos_encontrados.append(a.title())

def mostrar_todo():

    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for indice, archivo in enumerate(archivos_encontrados):
        print(f'{archivo}\t{numeros_encontrados[indice]}')
    print('\n')
    print(f'Números encontrados: {numeros_encontrados}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()
