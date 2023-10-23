# Ejercicios lección 5 - FUNCIONES DINÁMICAS

# Función que indica si hay algún nº de la lista entre 100 y 1000
def chequear_lista(lista):
    for n in lista:
        if n in range(100,1001):
            return True
        else:
            pass
    return False
resultado = chequear_lista([98,99,102])
print(resultado)

#Función que indica si hay algún nº de la lista entre 100 y 1000
def imprimir_lista(lista):
    lista_numeros = []
    for n in lista:
        if n in range(100,1001):
            lista_numeros.append(n) # con append metemos los nº en la lista_numeros
        else:
            pass
    return lista_numeros
resultado = imprimir_lista([23,12,98,376,102,532])
print(resultado)

# Función que devuelve FALSE si encuentra algún nº negativo y TRUE si todos son positivos
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
lista_numeros = todos_positivos([1,-50,502,-5000,755,600,33,61])
print(lista_numeros)

# Función que suma los números de una lista si están entre 1 y 1000
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(1,1000):
            suma += n
        else:
            pass
    return suma
lista_numeros = suma_menores([2,5,2,8])
print(lista_numeros)

# Función que cuenta la cantidad de numeros pares de una lista
def cantidad_pares(lista):
    cantidad = 0
    for n in lista:
        if n % 2 == 0:
            cantidad += 1
        else:
            pass 
    return cantidad
lista_numeros = cantidad_pares([2,3,4,5,6])
print(lista_numeros)

# Función que indica el precio más caro de los contenidos de un Tuple
precios_cafe = [('Capuchino',1.5),('Expreso',2),('Mocca',2.5)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return(cafe_mas_caro,precio_mayor)
cafe,precio = cafe_mas_caro(precios_cafe)

print(f"El café más cara es {cafe}\nPrecio: {precio}")