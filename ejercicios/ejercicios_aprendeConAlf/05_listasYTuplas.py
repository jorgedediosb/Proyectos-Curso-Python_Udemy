# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que almacene las asignaturas (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print(lista_asignaturas)

# 02. Escribir un programa que almacene asignaturas del anterior ejercicio y la muestre el mensaje
# 'Yo estudio <asignatura>', donde <asignatura> es cada una de las asignaturas de la lista.

lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
for asisgnatura in lista_asignaturas:
    print('Yo estudio', asisgnatura)

# 03. Escribir un programa que pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre: En <asignatura> has sacado <nota>
# donde <asignatura> es cada una des las asignaturas de la lista y <nota>.

lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
lista_notas = []
for asignatura in lista_asignaturas:
    notas = input(f'Escribe tu nota en {asignatura}: ')
    lista_notas.append(notas)
for posicion in range(len(lista_asignaturas)):
    print(f'\nEn {lista_asignaturas[posicion]} tienes un: {lista_notas[posicion]}')

# 04. Escribir un programa que pregunte los 6 nºs ganadores de la lotería,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros_ganadores = []
for i in range(6):
    numeros_ganadores.append(int(input("Introduce un número ganador: ")))
numeros_ganadores.sort()
print("Los números ganadores son: " + str(numeros_ganadores))

# 05. Escribir un programa que almacene en una lista los números del 1 al 10
# y los muestre por pantalla en orden inverso separados por comas.

list = [1,2,3,4,5,6,7,8,9,10]
# como una lista:
print(list[::-1])
# sin ser lista:
for i in reversed(list):
    print(i)
# sin ser lista y en una línea:
for i in range(1, 11):
    print(list[-i], end=',')

# 06. Escribir un programa que almacene las asignaturas de un curso en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura
# y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# opción 1:
lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
lista_asignaturas_aprobadas = []
for asignatura in lista_asignaturas:
    notas = float(input(f'Nota sacada en {asignatura}: '))
    if notas >= 5:
        lista_asignaturas_aprobadas.append(asignatura)
for asignatura in lista_asignaturas_aprobadas:
    #elimina de la lista general, las aprobadas para imprimir sólo las suspensas:
    lista_asignaturas.remove(asignatura)
print('Tienes que repetir: ' + str(lista_asignaturas))

#opción 2:
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#recorre del útimo al primero:
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        # eliminamos las materias aprobadas de la lista:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))

# 07. Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
#recorremos desde el último elemento hasta el 2º (sin incluir el primer elemento) 
for i in range(len(abecedario),1,-1):
    if i % 3 == 0:
        #El índice se resta 1 porque el índice de la lista comienzan en 0.
        abecedario.pop(i-1)
print(abecedario)

# 08. Escribir un programa que pida una palabra y muestre por pantalla si es un palíndromo.

palabra = input('Escribe una palabra: ')
#Recorremos la palabra del final al principio con [::-1]
palabra_invertida = palabra[::-1]
if palabra == palabra_invertida:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')

# 09. Escribir un programa que pida una palabra
# y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input('Palabra: ')
#opción 1:
print('Tu palabra tiene:')
print(f"Letra A: {palabra.count('a')}")
print(f"Letra E: {palabra.count('e')}")
print(f"Letra I: {palabra.count('i')}")
print(f"Letra O: {palabra.count('o')}")
print(f"Letra U: {palabra.count('u')}")
#opción 2:
vocales = ['a','e','i','o','u']
for vocal in vocales:
    repeticiones = 0
    for letra in palabra:
        if letra == vocal:
            repeticiones += 1
    print(f'la vocal {vocal} aparece {str(repeticiones)} veces')ç

# 10. Escribir un programa que almacene en una lista los siguientes precios:
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
# opcion 1:
lista = [50, 75, 46, 22, 80, 65, 8]
min = min(lista)
max = max(lista)
print(f'El precio mínimo es {min} y el máximo es {max}')
#opción 2:
min = max = lista[0]
for precio in lista:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print(f'El precio mínimo es {min} y el máximo es {max}')

# 11. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas
# y muestre su producto escalar.

a = (1,2,3)
b = (-1,0,2)
producto_escalar = 0
for i in range(len(a)):
    producto_escalar += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(producto_escalar))

# 12. Escribir un programa que almacene las matrices A=(123/456) y B =(-10/01/11) en una lista y muestre su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

# 13. Escribir un programa que pregunte por una muestra de números, separados por comas,
# los guarde en una lista y muestre su media y desviación típica (√(Σ(xi - μ)² / N)).

numeros = input("Introduce una muestra de números separados por comas: ")
numeros = numeros.split(',')
n = len(numeros)
for i in range(n):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)
suma = 0
sumasq = 0
for i in numeros:
    suma += i
    sumasq += i**2
media = suma/n
desviacion = (sumasq/n-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', desviacion)
