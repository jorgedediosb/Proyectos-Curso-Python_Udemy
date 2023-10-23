# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!

print('¡Hola Mundo!')

# 02. Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
# y luego muestre por pantalla el contenido de la variable.

mi_variable = 'Hola Mundo'
print(mi_variable)

# 03. Escribir un programa que pregunte el nombre del usuario en la consola
# y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
# donde <nombre> es el nombre que el usuario haya introducido.

nombre_usuario = input('¿Cómo se llamas? ')
print(f'Hola {nombre_usuario}!')

# 04. Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2*5)2.

print(((3+2)/(2*5))**2)

# 05. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

numero_horas = float(input('Horas trabajadas: '))
coste_horas = float(input('Coste por hora: '))
paga = numero_horas * coste_horas
print(f'Te corresponden {paga} euros')


# 06. Escribir un programa que lea un entero positivo, n, introducido por el usuario
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
# La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma=n(n+1)/2

user_number = int(input('Escribe un nº: '))
add = int(user_number * (user_number + 1) / 2)
print(f'La suma de los nºs anteriores al tuyo es: {add}')

# 07. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es <imc>
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
# IMC = (peso/altura)**2,2)
weight_user = float(input('Escribe tu peso en kg: '))
height_user = float(input('Escribe tu talla en metros: '))
imc = round((weight_user/height_user)**2,2)
print('Tu IMC es:', imc)

# 08. Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

user_number1 = int(input('Escribe un nº que será el dividendo: '))
user_number2 = int(input('Escribe un nº que será el divisor: '))
cociente = user_number1 / user_number2
resto = user_number1 % user_number2
print(f'{user_number1} entre {user_number2} da un cociente de {cociente} y un resto de {resto}.')

# 09. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

# Solicitar al usuario la cantidad a invertir, la tasa de interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
numero_anios = int(input("Ingrese el número de años: "))
# Convertir la tasa de interés anual de porcentaje a decimal:
tasa_interes_anual_decimal = tasa_interes_anual / 100
# Calcular el capital obtenido en la inversión:
capital_obtenido = round(cantidad_invertir * (1 + tasa_interes_anual_decimal) ** numero_anios)
print("El capital obtenido en la inversión es:", capital_obtenido)

# 10. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.

num_payasos = int(input('Payasos vendidos: '))
num_munecas = int(input('Muñecas vendidas: '))
peso_payasos = 112
peso_munecas = 75
total_payasos = num_payasos * peso_payasos
total_munecas = num_munecas * peso_munecas
total_kg = float((total_payasos + total_munecas)/100)
print(f'El peso total del paquete es: {total_kg} kg.')


# 11. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

deposito = float(input('Cantidad a depositar: '))
tasa_anual = 0.04
ahorros_ano1 = round(deposito * (1 + tasa_anual))
ahorros_ano2 = round(ahorros_ano1 * (1 + tasa_anual))
ahorros_ano3 =  round(ahorros_ano2 * (1 + tasa_anual))
print('Cantidad ahorros año 1: ', ahorros_ano1)
print('Cantidad ahorros año 2: ', ahorros_ano2)
print('Cantidad ahorros año 3: ', ahorros_ano3)

# 12. Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
barras_vendidas = int(input('Barras vendidas de otro día: '))
precio_barra = 3.49
descuento = 0.60
ventas_sin_descuento = barras_vendidas * precio_barra
ventas_con_descuento = ventas_sin_descuento * descuento
coste_total = round(ventas_sin_descuento - ventas_con_descuento)
print(f'Precio barra: {precio_barra}\nDescuento: {descuento}\nCoste final: {coste_total}')