# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/
'''
# 01. Escribir un programa que pida una palabra y la muestre por pantalla 10 veces.

palabra = input('Escribe una palabra y la repito x10: ')
for i in range(10):
    print(palabra)

# 02. Escribir un programa que la edad y muestre los años que ha cumplido (desde 1 hasta su edad).

edad = int(input('Edad: '))
for edad in range(1, edad + 1):
    print(edad)

# 03. Escribir un programa que pida un nº entero positivo
# y muestre todos los números impares desde 1 hasta ese número separados por comas.
number = int(input('Número: '))
output = ''
for i in range(1, number + 2, 2):
    if i < number:
        output += str(i) + ', '
    else:
        output += str(i) + '.'
print(output)
'''
# 04. Escribir un programa que pida un nº entero positivo
# y muestre la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input('Número: '))
output = ''
for i in range(number, -1, -1):
    if i != 0:
        output += str(i) + ','
    else:
        output = '0.'
print(output)

number = int(input('Número: '))
output = ''
for i in range(number, -1, -1):
    if i != 0:
        output += str(i) + ','
    else:
        output = '0.'
print(output)

