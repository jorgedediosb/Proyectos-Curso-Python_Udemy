# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 11. Generar un rango (lista) entre 0 y 10 (creciente).
rango = list(range(11))
print(rango)

# 12.1 Generar un número (rango) entre 5 y 10.
rango = list(range(5, 11))
print(rango)

# 12.2 Generar un número (aleatorio) entre 5 y 10.
import random
numero_aleatorio = random.uniform(5, 10) # nº con decimales
print(numero_aleatorio)
numero_aleatorio = round(numero_aleatorio, 2) # dejo el nº con 2 decimales
print(numero_aleatorio)

numero_aleatorio = random.randint(5, 10) # nº entero
print(numero_aleatorio)

# 13. Generar un rango de 10 a 0 (decreciente).
rango = list(range(10, 0, -1))
print(rango)

# 14. Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20.
print('OPCIÓNN 1 (rangos separados):')
rango1 = list(range(0, 11))
print(rango1)
rango2 = list(range(15, 21))
print(rango2)

print('OPCION 2 (rangos juntos):')
ambos_rangos = rango1 + rango2
print(ambos_rangos)

# 15. Generar un rango desde O hasta la longitud de la cadena "Hola mundo".
rango_palabra = list(range(0, len('Hola Mundo Viejuno')))
print(rango_palabra)