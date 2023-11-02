# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir una función que muestre el saludo ¡Hola amiga! cada vez que se la invoque.

def greet1():
    """La función muestra ¡Hola amiga!"""
    print('¡Hola amiga!')
    return
greet1()


# 02. Escribir una función a la que se le pase una cadena <nombre>
# y muestre el saludo ¡hola <nombre>!.

def greet2(nombre):
    """Función que muestra un saludo.
    Devuelve el saludo ¡Hola <nombre>!."""
    print('¡Hola ' + nombre +'!')
    return
greet2('Alf')


# 03. Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n):
    """Calcula el factorial de un número entero positivo."""
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp
print(factorial(4))

# 04. Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
# y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def invoice(amount, vat=21):
    """Función de aplica el IVA a una factura.
    Parametros: amount: Cantidad sin IVA / vat: Porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA."""
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))


# 05. Escribir una función que calcule el área de un círculo
# y otra que calcule el volumen de un cilindro usando la primera función.

def circle_area(radius):
    """Función que calcula el area de un círculo.
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius."""
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del cilindro de radio radius y altura high."""
    return circle_area(radius)*high

print(cilinder_volume(3,5))


# 06. Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def mean(sample):
    """Función que calcula la media de una muestra de números.
    sample: Es una lista de números
    Devuelve la media de los números en sample."""
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


# 07. Escribir una función que reciba una muestra de números en una lista
# y devuelva otra lista con sus cuadrados.

def square(lista_numeros):
    """Función que calcula los cuadrados de una lista de números.
    lista_numeros: Es una lista de números.
    Devuelve una lista con los cuadrados de los números de otra lista."""
    lista = []
    for i in lista_numeros:
        list.append(i**2)
    return lista

print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


# 08. Escribir una función que reciba una muestra de números en una lista
# y devuelva un diccionario con su media, varianza y desviación típica.

def square2(sample):
    """Función que calcula los cuadrados de una lista de números.
    sample: Es una lista de números.
    Devuelve una lista con los cuadrados de los números de la lista sample."""
    lista = []
    for i in sample:
        list.append(i**2)
    return lista

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample."""
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square2(sample))/len(sample) - stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


# 09. Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.

def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m."""
    rest = 0
    while m > 0:
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m."""
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))


# 10. Escribir una función que convierta un número decimal en binario
# y otra que convierta un número binario en decimal.

def to_decimal(n):
    """Función que convierte un número binario en decimal.
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n."""
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    """Función que convierte un número decimal en binario.
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n."""
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))


# 11. Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia."""
    texto = texto.split()
    words = {}
    for i in texto:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(texto))
print(most_repeated(count_words(texto)))

