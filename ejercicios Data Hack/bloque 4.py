# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 16. Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas
# y con los 2 primeros CARACTERES INTERCAMBIADOS. Por ejemplo, hola mundo pasaría a mula hondo.
cadena1 = input('Dame la primera cadena: ')
cadena2 = input('Dame la segunda cadena: ')
print(cadena2[:2] + cadena1[2:] + "" + cadena1[:2] + cadena2[2:]) # [:2] coge las 2 primeras letras y [2:] coge el resto de letras a partir de la 3ª

# 17. Pide una cadena e indica si es un PALÍNDROMO o no.
cadena1 = input('Escribe un texto: ')
palindromo = cadena1[::-1] #doy 'la vuelta' a cadena1 para crear el texto al revés
print(f'Tu texto al revés es: {palindromo}')
if (cadena1 == palindromo):
    print('Tu texto es un palíndromo')
else:
    print('Tu texto no es un palíndromo')
