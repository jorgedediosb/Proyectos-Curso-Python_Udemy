# Ejercicios lección 5 - INTERACCIÓN FUNCIONES "Tirar Moneda"

# Función que devuelve el resultado de lanzar una moneda.
# Debe devolver resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

import random

def lanzar_moneda():
    resultado = random.choice(["cara", "cruz"])
    return resultado

def probar_suerte(resultado_moneda,lista_numeros):
    if resultado_moneda == "cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "cruz":
        print("La lista fue salvada")
        return lista_numeros
    
lista_numeros = [1,2,3,4,5]
resultado_moneda = lanzar_moneda()
lista_resultante = probar_suerte(resultado_moneda,lista_numeros)

print(resultado_moneda)
print(lista_resultante)