#Ejercicios lección 4 - RANGO

lista = [1,2,3,4]
for numeros in lista:
    print(numeros)

for numeros in range(5):
    print(numeros)

for numeros in range(20, 31):
    print(numeros)

for numeros in range(20, 31, 2):
    print(numeros)

#forma sencilla de imprimir una lista extensa usando range
lista1 = list(range(0,101))
print(lista1)

#lista con todos los nºs múltiplos de 3, del 3 al 300 
lista2 = list(range(3,301,3))
print(lista2)

# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive).
suma_cuadrados = 0
for numeros in range(1,16):
    suma_cuadrados = suma_cuadrados + numeros**2
print(suma_cuadrados)