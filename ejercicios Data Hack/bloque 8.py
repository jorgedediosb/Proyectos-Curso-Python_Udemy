# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 26. Definir una función superposicion() que tome dos listas
# y devuelva True si tienen al menos 1 elemento en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.

print('EJERCICIO 26:')
def superposicion(lista1, lista2):
    for x in lista1:
        for y in lista2:
            if x == y:
                return True
            else:
                return False

mi_lista1 = [1,2,3]
mi_lista2 = [1,2,3]
print(superposicion(mi_lista1, mi_lista2))


# 27. Definir una función generar_n_caracteres() que tome un entero n
# y devuelva el caracter multiplicado por n.
# Por ejemplo: generar__caracteres(5, "×") debería devolver "xxxxx".

print('\nEJERCICIO 27:')

print('Opción 1:')
def generar_n_caracteres(n, caracter):
    print(n * caracter)

generar_n_caracteres(5, 'x')

print('Opción 2:')
def generar_multiplicacion(n):
    print(n ** n)

generar_multiplicacion(5)

# 28. Definir un histograma procedimiento() que tome una lista de números enteros
# e imprima un histograma en la pantalla.
# Ejemplo: procedimiento ([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******

print('\nEJERCICIO 28:')
def procedimiento(lista):
    for n in lista:
        print(n * '*')

mi_lista = ([4, 9, 7])
procedimiento(mi_lista)

# 29. La función max() y la función max_de_tres() (ejercicios 19 y 20), solo van a funcionar para 2 o 3 números.
# Supongamos que tenemos más de 3 números o no sabemos cuántos números son.
# Escribir una función max_in_list() que tome una lista de números y devuelva el más grande.

print('\nEJERCICIO 29:')
def max_in_list(lista):
    #Excepción para una lista vacía:
    if not lista:
        return None
    max_valor = lista[0]
    for n in lista:
        if n > max_valor:
            max_valor = n
    return max_valor

mi_lista = [4,3,6,7,2,1]
print(max_in_list(mi_lista))

# 30. Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.

def mas_larga(lista):
    #Excepción lista vacía:
    if not lista:
        return None
    palabra_mas_larga = lista[0]
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

mi_lista = ['pato', 'conejo', 'cocodrilo']
print(mas_larga(mi_lista))