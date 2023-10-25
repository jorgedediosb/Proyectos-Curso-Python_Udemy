# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/
'''
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
'''
# 07. Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

