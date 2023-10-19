# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 19. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(n1, n2):
    if n1 > n2:
        print(n1)
    elif n1 > n2:
        print(n2)
    else:
        print('Los números son iguales')


# 20. Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print('Los números son iguales')


# 21. Definir una función que calcule la longitud de una lista o una cadena dada.
# Que haga lo que hace len()

def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

mi_lista = [0,1,2,3,4,5,6]
longitud = largo_cadena(mi_lista)
print(f'La longitud de mi lista es de {longitud} elementos.')


# 22. Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False.

def es_vocal(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    elif x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        return True
    else:
        return False

mi_letra = 'j'
print(es_vocal(mi_letra))

# 23. Escribir una función sum() y una función multip()
# que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

