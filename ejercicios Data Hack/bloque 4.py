# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

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
