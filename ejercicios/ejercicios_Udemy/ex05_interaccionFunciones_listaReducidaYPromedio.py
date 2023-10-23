# Ejercicios lección 5 - INTERACCIÓN FUNCIONES "Lista Reducida y Promedio"

# función que tome una lista como argumento y devuelva la misma lista, eliminando duplicados y eliminando el valor más alto

# Usando set() para ordenar los nºs ,max() para buscar el máximo nº y remove() para eliminarlo
def reducir_lista(lista):
    lista_sin_repetidos = list(set(lista))
    maximo_valor = max(lista_sin_repetidos)
    lista_sin_repetidos.remove(maximo_valor)
    return lista_sin_repetidos

lista_numeros = [1,1,2,2,3,5,5,8]
lista_reducida = reducir_lista(lista_numeros)

print(lista_reducida)

# Usando sort, para ordenar la lista sin repetir nºs y pop() para emilinar el último nº
def reducir_lista(lista):
    lista_sin_repetidos = list(set(lista))
    lista_sin_repetidos.sort()
    lista_sin_repetidos.pop()
    return lista_sin_repetidos

lista_numeros = [1,1,2,2,3,5,5,8]
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)

def promedio(lista):
    suma = sum(lista)
    cantidad_items = len(lista)
    promedio = suma / cantidad_items
    return promedio

resultado_promedio = promedio(lista_reducida)
print(resultado_promedio)