#Ejercicios lección 4 - Bucles / loops - FOR

#Bucle FOR:
lista = ['a', 'b', 'c']
for letra in lista:
    print("letra: " + letra)
print(lista)

lista = [1, 2, 3]
for num in lista:
    num_lista = lista.index(num) + 1 #Al empezar en la posición del index 0, hay que sumar 1.
    print(f"Posición {num_lista} en la lista es {num}")

#buscar una característica en una lista de string con for:
lista = ['pedro','jorge','elena','cristina']
for nombre in lista:
    if nombre.startswith('e'):
        print(f"Nombres que empiezan con la letra 'e': ", nombre)

#sumar números de una lista con for:
numeros = [1,2,3,4,5]
suma = 0
for numero in numeros:
    suma = suma + numero
print(suma) #si no lo indentamos correctamente (fuera del for) el resultado es distinto

#imprimir con for:
palabra = 'python'
for letras in palabra:
    print(letras)

for letras in ' jorge': #indicamos el string directamente (sin meterlo en una variable). Esto lo podemos hacer con cualquier otro objeto (lista, tuple, etc)
    print(letras)

for a in [[1,2], [3,4],[5,6]]:
    print(a)

for a,b in [[1,2], [3,4],[5,6]]:
    print(a)

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}
for item in dic.values(): #indicando 'items' imprimimos las clavas y los valores
    print(item)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumnos in alumnos_clase:
    print("Hola " + alumnos)

#Suma los pares y los impares de la lista de números:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numeros in lista_numeros:
    if numeros % 2 == 0:
        suma_pares = suma_pares + numeros
    else:
        suma_impares = suma_impares + numeros
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")

#uso de break:
nombre = input("Escribe tu nombre sin r: ")
for letras in nombre:
    if 'r' in nombre: #Si el nombre tiene 'r' no lo imprime
        break #break detiene el bucle
    print(letras)

nombre = input("Escribe un país: ")
for letras in nombre:
    if letras == 'r':
        break
    print(letras)