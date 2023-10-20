# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 24. Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

print('EJERCICIO 24:')

print('OPCIÓN 1:')
def inversa(cadena):
    #Usando la transformación a palíndromo:
    cadena_inversa = cadena[::-1]
    print(cadena_inversa)

mi_cadena = 'estoy probando'
inversa(mi_cadena)

print('OPCIÓN 2:')
def invesa(cadena):
    invertida = ""
    #Usando la función len:
    cont = len(cadena)
    # -1 para acceder a la cadena desde el final:
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

mi_cadena = 'estoy probando'
inversa(mi_cadena)

# 25. Definir una función es_palindromo() que reconoce palíndromos
# ejemplo: es_palindromo ("radar") tendría que devolver True.

print('\nEJERCICIO 25:')

print('OPCIÓN 1:')
def es_palindromo(cadena):
    #Convierto la cadena a minúsculas para evitar problemas con mayúsculas:
    cadena = cadena.lower()
    palindromo = cadena[::-1]
    if cadena == palindromo:
        print('Tu cadena es un palindromo.')
        return True
    else:
        print('Tu cadena NO es un palíndromo.')
        return False

mi_cadena = 'radar'
#Para imprimir True o False:
resultado = es_palindromo(mi_cadena)
print(resultado)

print('\nOPCIÓN 2:')

def inversa(cadena):
    invertida = ''
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range(len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            return False
            break
    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorrió todo el ciclo for y todas las letras son iguales
        return True

mi_cadena = 'radar'
#Para imprimir True o False:
resultado = es_palindromo(mi_cadena)
print(resultado)