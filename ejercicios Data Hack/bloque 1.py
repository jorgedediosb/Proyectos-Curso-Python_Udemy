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
