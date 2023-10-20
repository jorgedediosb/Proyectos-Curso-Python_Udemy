# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 19. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

print('EJERCICIO 19')

def max(n1, n2):
    if n1 > n2:
        print(f'{n1} es mayor que {n2}.')
    elif n2 > n1:
        print(f'{n2} es mayor que {n1}.')
    else:
        print('Los números son iguales')

n1 = int(input('Escribe un nº: '))
n2 = int(input('Escribe otro nº: '))
max(n1, n2)

# 20. Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

print('\nEJERCICIO 20')

def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print('El nº mayor es', n1)
    elif n2 > n1 and n2 > n3:
        print('El nº mayor es', n2)
    elif n3 > n1 and n3 > n2:
        print('El nº mayor es', n3)
    else:
        print('Los tres números son iguales')

n1 = int(input('Escribe el 1er nº: '))
n2 = int(input('Escribe el 2º nº: '))
n3 = int(input('Escribe el 3er nº: '))
max_de_tres(n1, n2, n3)



# 21. Definir una función que calcule la longitud de una lista o una cadena dada.
# Que haga lo que hace len()

print('\nEJERCICIO 21')

def largo_cadena(lista):
    cont = 0
    for n in lista:
        cont += 1
    return cont

mi_lista = [0,1,2,3,4,5,6]
longitud = largo_cadena(mi_lista)
print(f'La longitud de la lista es de {longitud} elementos.')


# 22. Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False.

print('\nEJERCICIO 22')

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

print('\nEJERCICIO 23')

def suma(lista):
    sum = 0
    for n in lista:
        sum += n
    return sum

def multiplicar(lista):
    mult = 1
    for n in lista:
        mult *= n
    return mult

mi_lista = [1, 2, 3, 4]
print(f'la suma total de la lista es {suma(mi_lista)}')
print('la multiplicación total de la lista es', multiplicar(mi_lista))