# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 32. Escribir un programa que diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene.

print('EJERCICIO 32:')
def cuantas_mayusculas(cadena):
    num_mayusc = 0
    for caracter in cadena:
        #Busca mayúsculas con las minúsculas (distinto a)
        if caracter != caracter.lower():
            num_mayusc += 1
    return num_mayusc

cadena_usuario = input('Ingresa un texto para contar las mayúsculas: ')
resultado = cuantas_mayusculas(cadena_usuario)
print(f'Tu texto tiene {resultado} mayúscula/s')


# 33. Construir un pequeño programa que convierta números binarios en enteros.

print('\nEJERCICIO 33:')
def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len(numeroBin) -1
    for i in numeroBin:  
        decimal += (int(i) * 2**(exp))
        # Se resta 1 xq en binario, la posición más a la derecha es 2^0, la siguiente es 2^1
        exp = exp - 1
    return(decimal)

mi_decimal = 1010
print(aDecimal(mi_decimal))


# 34. Escribir un pequeño programa donde:
# • Se ingresa el año en curso.
# • Se ingresa el nombre y el año de nacimiento de tres personas.
# • Se calcula cuántos años cumplirán durante el año en curso.
# • Se imprime en pantalla.

print('\nEJERCICIO 34:')
def cuantos_anos():
    ano_actual = int(input('¿En qué año estamos?: '))
    #El bucle se repite tres veces, uno por usuario:
    for n in range(3):
        nombre_usuario = input('¿Cómo te llamas?: ')
        ano_nacimiento = int(input('¿Qué año naciste?: '))
        anos_cumplidos = ano_actual - ano_nacimiento
        print(nombre_usuario, 'cumple o tiene', anos_cumplidos, 'años')

cuantos_anos()


# 35. Definir una tupla con 10 edades de personas.
# Imprimir la cantidad de personas con edades superiores a 20.

print('\nEJERCICIO 35:')
def mayorA20(tupla):
    personas = 0
    for p in tupla:
        if p > 20:
            personas += 1
    return personas

mi_tupla = (15, 20, 25, 74, 19, 0)
resultado = mayorA20(mi_tupla)
print(f'en la tupla hay {resultado} persona/s mayores de 20')


# 36. Definir una lista con un conjunto de nombres.
# Imprimir la cantidad de comienzan con la letra a.
# También se puede elegir al usuario la letra a buscar.

print('\nEJERCICIO 36:')

print('Opción 1:')

nombres = ["Ana", "Carlos", "Pedro", "Alicia", "Juan", "Marta"]

letra = input("Ingresa la letra para buscar nombres que comienzan con esa letra: ")

conteo = 0
for nombre in nombres:
    if nombre.lower().startswith(letra.lower()):
        conteo += 1

print(f"La cantidad de nombres que comienzan con la letra '{letra}' es: {conteo}")


print('Opción 2:')
def empiezanPor():
    numero_nombres = int(input("¿Cuántos nombres quieres ingresar?: "))
    lista = []
    for n in range(numero_nombres):
        nombre = input("Ingresa el nombre: ")
        lista.append(nombre)
    print("")
        
    letra = input ("Con qué letra empieza el nombre?: ")
    letras = 0
    for n in lista:
        if n[0] == letra.lower() or n[0] == letra.upper():
                letras += 1
    return letras

cantidad = empiezanPor()
print(f"La cantidad de nombres que comienzan con la letra ingresada es: {cantidad}")


# 37. Crear una función contar_vocales(), que reciba una palabra
# y cuente cuantas letras "a", "e", etc tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

print('\nEJERCICIO 37:')

def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    for x in vocales:
        contador = 0
        for i in palabra:
            if i == x:
                contador += 1
        print("Hay %d %s." % (contador, x))

mi_palabra = 'Jorge'
print(contar_vocales(mi_palabra))

# 38. Escriba una función es bisiesto() que determine si un año determinado es un año bisiesto.
# Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400.

print('\nEJERCICIO 38:')

def es_bisiesto():
    a = int(input("Escriba un año y le dire si es bisiesto: "))
    if (a % 4 == 0) and (not(a % 100 == 0)):
        print("El año", a, "es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print("El año", a, "es un año bisiesto porque es multiplo de 400")
    else:
        print("El año", a, "no es bisiesto")

es_bisiesto()