# Ejercicios extraídos de: https://es.slideshare.net/uni_fcys_sistemas/ejercicios-resueltos-con-python

# 1. Imprimir "Hola mundo" por pantalla.
print('hola mundo')

# 2. Crear dos variables numéricas, sumarlas y mostrar el resultado.
var1 = 5
var2 = 10
suma = var1 + var2
print("la suma de", var1, "y", var2, "es", suma)

# 3. Mostrar el precio del IVA de un producto con un valor de C$100.00 y su precio final.
precio_producto = float(100) # transformo 100 a float
iva = 0.15
precio_iva = precio_producto * iva
print('El precio del producto sin iva es:', precio_producto, '$')
print('El precio del producto con iva es:', (precio_iva + precio_producto), '$')

# 4. De dos números, saber cuál es el mayor.
a = 8
b = 7
if a > b:
    print(f'{a} es MAYOR que {b}')
else:
    print(f'{a} es MENOR que {b}')

# 5. Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
a = 11
if a >= 0 and a <= 10:
    print('el número está entre 0 y 10, el número es', a)
else:
    print('el número NO está entre 0 y 10, el número es', a )


def es_bisiesto():
    print("Comprueba años bisiestos")
    a = input ("Escriba un año y le dire si es bisiesto: ")
    if (a % 4 == 0) and (not(a % 100 == 0)):
        print("El año", a, "es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print("El año", a, "es un año bisiesto porque es multiplo de 400")
    else:
        print("El año", a, "no es bisiesto")

es_bisiesto()


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