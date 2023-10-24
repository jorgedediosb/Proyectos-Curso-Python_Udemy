'''

# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que pregunte el nombre del usuario en la consola y un nº entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el nº introducido.

# Opción 1:
nombre = input('Escribe tu nombre: ')
numero = int(input('Escribe un nº entero: '))
for n in range(numero):
    print(nombre)

# Opción 2 (con salto de línea al final):
nombre = input('Escribe tu nombre: ')
numero = int(input('Escribe un numero: '))
print((nombre + '\n')* numero)

# 02. Escribir un programa que pregunte el nombre completo del usuario en la consola
# y después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, otra con todas las letras mayúsculas
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input('Escribe tu nombre completo: ')
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

# 03. Escribir un programa que pregunte el nombre del usuario en la consola
# y después muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre = input('Escribe tu nombre: ')
letras_nombre = len(nombre)
nombre_mayus = nombre.upper()
#Opción 1:
print(f'{nombre_mayus} tiene {letras_nombre} letras.')
#Opción 2:
print(nombre.upper() + ' tiene ' + str(len(nombre)) + ' letras.')

# 04. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que muestre el número de teléfono sin el prefijo y sin la extensión.

telefono = input('Escribe el nº telf: ')
#Opción 1:
partes = telefono.split('-')
print(partes[1])
#Opción 2:
print(telefono[4:-3])

# 05. Escribir un programa que pida al usuario que introduzca una frase en la consola
# y muestre por pantalla la frase invertida.

frase = input('Escribe una frase: ')
#Opción 1:
frase_invertida = ''.join(reversed(frase))
print(frase_invertida)
#Opción 2:
print(frase[::-1])

# 06. Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
# si la vocal no está en la frase debe decírselo al usuario y debe escribir otra vocal

frase = input('Escribe una frase: ')
vocal = input('Escribe una vocal: ')

def letra_mayus():
    print(frase.replace(vocal, vocal.upper()))

while vocal not in frase:
    print('Esa vocal no está en la frase.')
    vocal = input('Escribe otra vocal: ')

letra_mayus()

# 07. Escribir un programa que pregunte el correo electrónico del usuario
# y muestre otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

email = input('Escribe tu mail: ')
#Opción 1:
partes_email = email.split('@')
email_ceu = partes_email[0] + '@ceu.es'
print(email_ceu)
#Opción 2:
print(email[:email.find('@')] + '@ceu.es')

# 08. Escribir un programa que pregunte el precio de un producto en euros con dos decimales
# y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input('Precio (dos decimales): ')
euros = precio[:precio.find('.')]
centimos = precio[precio.find('.')+1:]
print('Los euros son:', euros, '€', ' y los centimos son:', centimos, 'cents')

# 09. Escribir un programa que pregunte la fecha de su nacimiento en formato dd/mm/aaaa
# y muestra el día, el mes y el año.
# Adaptar el programa anterior para que funcione cuando el día o el mes se introduzcan con un solo carácter.

#Opción 1:
fecha = input('Fechas de nacimiento (dd/mm/aaaa): ')
dia = fecha[:2]
mes = fecha[3:5]
ano = fecha[6:]
print('El día es:', dia, ', el mes es:', mes, 'y el año es:', ano)
#Opción 2:
fecha = input('Fechas de nacimiento (d/m/aaaa): ')
fecha_partida = fecha.split('/')
dia = fecha_partida[0]
mes = fecha_partida[1]
ano = fecha_partida[2]
print('El día es:', dia, ', el mes es:', mes, 'y el año es:', ano)

# 10. Escribir un programa que pregunte por los productos de una cesta de la compra, separados por comas,
# y muestre por pantalla cada uno de los productos en una línea distinta.

compra = input('¿Qué has comprado Momi? (sepáralo por comas): ')
#Opción 1:
print(compra.replace(',', '\n'))
#Opción 2:
print('\n'.join(compra.split(',')))
#Opción 3:
lista_compra = compra.split(',')
for n in lista_compra:
    print(n)

'''
# 11. Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
# y muestre una cadena con el nombre del producto seguido de:
# su precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos
# y el coste total con 8 dígitos enteros y 2 decimales.



