# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 11. Generar un rango (lista) entre 0 y 10 (creciente).
print('EJERCICIO 11')
rango = list(range(11))
print(rango)

# 12.1 Generar un rango (lista) entre 5 y 10 (incluyendo el 5 y el 10).
print('EJERCICIO 12')
rango = list(range(5, 11))
print(rango)

# 12.2 Generar un número (aleatorio) entre 5 y 10 (incluyendo el 5 y el 10).
import random
# nº con varios decimales:
numero_aleatorio = random.uniform(5, 10) 
print(numero_aleatorio)
 # El nº con varios decimales se reduce a 2 decimales:
numero_aleatorio = round(numero_aleatorio, 2)
print(numero_aleatorio)
# nº entero:
numero_aleatorio = random.randint(5, 10)
print(numero_aleatorio)

# 13. Generar un rango de 10 a 0 (decreciente).
print('EJERCICIO 13')
rango = list(range(10, 0, -1))
print(rango)

# 14. Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20.
print('EJERCICIO 14')
print('OPCIÓNN 1 (rangos separados):')
rango1 = list(range(0, 11))
print(rango1)
rango2 = list(range(15, 21))
print(rango2)

print('OPCION 2 (rangos juntos):')
ambos_rangos = rango1 + rango2
print(ambos_rangos)

# 15. Generar un rango desde O hasta la longitud de la cadena "Hola mundo".
print('EJERCICIO 15')
rango_palabra = list(range(0, len('Hola Mundo Viejuno')))
print(rango_palabra)


# 16. Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas
# y con los 2 primeros CARACTERES INTERCAMBIADOS. Por ejemplo, hola mundo pasaría a mula hondo.
print('EJERCICIO 16:')
cadena1 = input('Dame la primera cadena de texto: ')
cadena2 = input('Dame la segunda cadena de texto: ')
#[:2] coge las 2 primeras letras y [2:] coge el resto de letras a partir de la 2ª:
print(cadena2[:2] + cadena1[2:] + "" + cadena1[:2] + cadena2[2:])


# 17. Pide una cadena e indica si es un PALÍNDROMO o no.
print('EJERCICIO 17:')
cadena1 = input('Escribe un texto: ')
#Se da 'la vuelta' a cadena con [::-1] para crear el texto al revés:
palindromo = cadena1[::-1]
print(f'Tu texto al revés es: {palindromo}')
if (cadena1 == palindromo):
    print('Tu texto es un palíndromo.')
else:
    print('Tu texto no es un palíndromo.')
