# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir una función que aplique un descuento a un precio
# y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios
# y porcentajes de una cesta de la compra, y una de las funciones anteriores,
# y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta
# y devolver el precio final de la cesta.

def apply_discount(price, discount):
    '''
    Función que aplica un descuento a una cantidad.
        price: Es un valor real con el precio al que aplicar el descuento.
        discount: Es el porcentaje a descontar.
    Devuelve:
        El precio final tras aplicar el descuento.
    '''
    return price - price * discount / 100
    
def apply_IVA(price, percentage):
    '''
    Función que aplica un IVA a una cantidad.
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))


# 02. Escribir una función que simule una calculadora científica que permita calcular
# el seno, coseno, tangente, exponencial y logaritmo neperiano.
# La función preguntará al usuario el valor y la función a aplicar,
# y mostrará una tabla con los enteros de 1 al valor introducido
# y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log

def apply_function(f, n):
    '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
    · f: Es una función que recibe un número real y devuelve otro.
    · n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    '''
    Función que aplica una función seleccionada por el usuario
    (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros
    y el resultado de aplicarles la función introducida.
    · f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).
    · n: Es un entero positivo.
    '''
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()

# 03. Escribir una función que reciba otra función y una lista,
# y devuelva otra lista con el resultado de aplicar la función dada
# a cada uno de los elementos de la lista.

def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.
    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))


# 04 . Escribir una función que reciba otra función booleana y una lista,
# y devuelva otra lista con los elementos de la lista que devuelvan
# True al aplicarles la función booleana.

def filtra_lista(funcion, lista):
    '''Función que filtra los elementos de una lista que devuelven true al aplicarle una función booleana.
        - funcion: Es una función booleana (devuleve true o false)
        - lista: Es una lista con valores que se pasarán como argumentos a funcion.
        Devuelve:
        Una lista con los elementos de la lista que devuelven true al aplicarles la función booleana.
    '''
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(filtra_lista(par, [1, 2, 3, 4, 5, 6]))


# 05. Escribir una función que reciba una frase y devuelva un diccionario
# con las palabras que contiene y su longitud.

def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    words = sentence.split()
    lengths = map(len, words)
    # Opción 1:
    return dict(zip(words, lengths))
    # Opción 2:
    # return {word:len(word) for word in sentence.split()}

print(length_words('Welcome to Python'))


# 06. Escribir una función reciba una lista de notas
# y devuelva la lista de calificaciones correspondientes a esas notas.

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))
    # Opción 2:
    # return [grade(x) for x in scores]
print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))


# 07. Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno
# y devuelva otro diccionario con las asignaturas en mayúsculas
# y las calificaciones correspondientes a las notas.

def grade1(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade1(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas
    y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:
        calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))

print(apply_grade1({'Matemáticas':6.5, 'Física':5, 'Química':3.4,
                    'Economía':8.2, 'Historia':9.7, 'Programación':10}))


# 08. Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno
# y devuelva otro diccionario con las asignaturas en mayúsculas
# y las calificaciones correspondientes a las notas aprobadas.

def grade2(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def passed_subject(subject):
    '''
    Función que recibe una tupla con una asignatura y su nota
    y devuelve True si la asignatura está aprobada o False si está suspensa.abs
    Parámetros:
        subject: Es una tupla (asignatura, nota) donde nota es un valor real entre 0 y 10.
    Devuelve: True si la nota es mayor o igual que 5 y False si no.abs
    '''
    return subject[1] >= 5

def apply_grade2(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas
    y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es
        la calificación correspondiente a la nota de la asignatura.
    '''
    passed = dict(filter(passed_subject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade2, passed.values())
    return dict(zip(subjects, grades))

print(apply_grade2({'Matemáticas':6.5, 'Física':5, 'Química':3.4,
                    'Economía':8.2, 'Historia':9.7, 'Programación':10}))

# 09. Escribir una función que calcule el módulo de un vector.

def sum_square(x, y):
    '''
    Función que recibe dos valores y calcula la suma del primero más el cuadrado del segundo.
    Parámetros:
        x: Es un número real.
        y: Es un número real.
    Devuelve:
        x + y²
    '''
    return x + y ** 2

def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    # opción 1:
    from functools import reduce
    return reduce(sum_square, v, 0) ** 0.5
    # opción 2 (elininando la función def sum_square(x, y)):
    # return sum([x ** 2 for x in v]) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))

# 10. Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
"""
[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
"""
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio,
# y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado.
# Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario
# con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:
# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro,map(añadir_precio, pisos)))

print(busca_piso(pisos, 100000))


# 11. Escribir una función que reciba una muestra de números y devuelva los valores atípicos,
# es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3.
# Nota: La puntuación típica de un valor se obtiene restando la media
# y dividiendo por la desviación típica de la muestra.

from statistics import mean, stdev

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def f(n):
        puntuacion = (n - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))

