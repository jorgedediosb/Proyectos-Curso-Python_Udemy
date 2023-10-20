# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 6. Añadir al ejercicio anterior, que si está entre 11 y 20 muestre otro mensaje diferente
# si está entre 21 y 30 otro mensaje.
numero = int(input('Escribe un número: '))
if numero >= 0 and numero <= 10:
    print('En número está entre 0 y 10, el número es', numero)
elif numero >= 11 and numero <= 20:
    print('En número está entre 11 y 20, el número es', numero)
elif numero >= 21 and numero <= 30:
    print('En número está entre 21 y 30, el número es', numero)
else:
    print('El número es mayor a 30, el número es', numero)

# 7. Usar un while para mostrar los números del 1 al 100.
n = 1
while n <= 100:
    print(n)
    n += 1
print('FIN BUCLE WHILE')

# 8. Mostrar con un for los números del 1 al 100.
for n in range(1, 101):
    print(n)
print('FIN BUCLE FOR')

# 9. Mostrar los caracteres de la cadena "Hola mundo".
for c in 'Hola Mundo':
    print(c)

# 10. Mostrar los números pares entre 1 al 100.
print('FORMA 1:')
for n in range(1, 101):
    if(n % 2 == 0):
        print(n)

print('FORMA 2:')
for n in range(2, 101, 2):
    print(n)