# Ejercicios lección 5 - INTERACCIÓN FUNCIONES "Lista Reducida"

# función que tome una lista como argumento y devuelva la misma lista, eliminando duplicados y eliminando el valor más alto
def reducir_lista(lista):
    lista_sin_repetidos = list(set(lista))
    maximo_valor = max(lista_sin_repetidos)
    lista_sin_repetidos.remove(maximo_valor)
    return lista_sin_repetidos

def promedio(lista):
    suma = sum(lista)
    cantidad_items = len(lista)
    promedio = suma / cantidad_items
    return promedio

lista_numeros = [1,1,2,2,3,5,5,8]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

print(lista_reducida)
print(resultado_promedio)