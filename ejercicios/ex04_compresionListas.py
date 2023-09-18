# Ejercicios lección 4 - COMPRESIÓN LISTAS

# Antes para crear una lista desde otro objeto hacíamos:
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# Podemos comprimir la lista:
palabra = 'python'
lista = [letra for letra in palabra]
print(lista)

# Podemos comprimir aún más:
lista = [palabra for palabra in 'python']
print(lista)

# Esto admite rangos:
lista = [n for n in range(0,21,2)]
print(lista)

# Inlcuso admite condicionales:
lista = [n for n in range(0,21,5)if n*2 > 10]
print(lista)

# Si queremos añadir más condicionales:
lista = [n if n*2 > 10 else 'no' for n in range(0,21,5)] # Si n*2 no es > 10, imprime 'no'
print(lista)

# Elevamos al cuadrado los nºs de la lista valores
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numeros**2 for numeros in valores]
print(valores_cuadrado)

# Imprimimos sólo los nºs pares
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)

# Imprimimos los grados Celsius a partir de lista con grados Fahrenheit
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celsius)