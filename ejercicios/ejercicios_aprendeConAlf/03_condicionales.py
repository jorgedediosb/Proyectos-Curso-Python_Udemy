# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('Escribe tu edad: '))
if edad >= 18:
    print('Eres mayor de edad!')
else:
    print('Eres menor de edad.')

# 02. Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pida otra contraseña
# e imprima si la contraseña coincide con 'contraseña' sin tener en cuenta mayúsculas y minúsculas.

key = 'contraseña'
password = input('Escribe tu contraseña: ')
if key == password.lower():
    print('Tu contraseña coincide')
else:
    print('Tu contraseña NO coincide')

# 03. Escribir un programa que pida dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

def division(num1, num2):
    while num2 == 0:
        print('Tu nº no debe ser cero.')
        num2 = float(input('Escribe otro nº: '))
    else:
        resultado = num1 / num2
        print(f'El resultado de la división es: ', resultado)

num1 = float(input('Escribe un nº: '))
num2 = float(input('Escribe otro nº: '))

division(num1, num2)

# 04. Escribir un programa que pida un nº entero y muestre por pantalla si es par o impar.

numero = int(input('Escribe un nº: '))
if numero % 2 == 0:
    print('Tu nº es par.')
else:
    print('Tu nº es impar.')

# 05. Para tributar impuesto hay que ser mayor de 16 años y tener ingresos iguales o superiores a 1000€/mes.
# Escribir un programa que pregunte edad e ingresos mensuales
# y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input('Edad: '))
ingresos = input('Ingresos/mes: ')
#añado la opción de indicar miles con '.' (2.000 = 2000)
ingresos = ingresos.replace('.','')
ingresos = float(ingresos)

if edad > 16 and ingresos >= 1000:
    print('Debes tributar! Hacienda somos todos.')
else:
    print('No tienes que tributar.')

# 06. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A son las mujeres con nombre anterior a la M y hombres con nombre posterior a la N
# y el grupo B por el resto.
# Escribir un programa que pregunte nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input('Nombre: ')
sexo = input('Sexo(m/f): ')
# opción sexo en mayus o min:
sexo = sexo.lower()

if (nombre[0] < 'M' and sexo == 'f') or (nombre[0] > 'N' and sexo == 'm'):
    print('Estás en el grupo A')
else:
    print('Estás en el grupo B')

# 07. Escribir un programa que pregunte renta anual y muestre por pantalla el tipo impositivo que le corresponde.
# Los tramos impositivos son los siguientes:
# Menos de 10000€ - 5% / Entre 10000€ y 20000€ - 15% / Entre 20000€ y 35000€ - 20% / Entre 35000€ y 60000€ - 30% / Más de 60000€ - 45%

renta = input('Renta anual: ')
# opción poner miles (2.000 = 2000)
renta_str = renta.replace('.','')
renta = float(renta_str)

if renta < 10000:
    print('Tipo impositivo: 5%')
elif renta >= 10000 and renta <= 20000:
    print('Tipo impositivo: 15%')
elif renta > 20000 and renta <= 35000:
    print('Tipo impositivo: 20%')
elif renta > 35000 and renta <= 60000:
    print('Tipo impositivo: 30%')
else:
    print('Tipo impositivo: 45%')

# 08. En una empresa, sus empleados son evaluados al final de cada año.
# Los puntos en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ por la puntuación del nivel.
# Tabla puntuación: Nivel Puntuación: Inaceptable	- 0.0 / Aceptable - 0.4 / Meritorio - 0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

bonificacion = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input('¿Cuántos puntos tienes?: '))
if puntos == inaceptable:
    nivel = 'Inaceptable'
elif puntos == aceptable:
    nivel = 'Aceptable'
elif puntos >= 0.6:
    nivel = 'Meritorio'
else:
    nivel = ''
if nivel == '':
    print('Tu nivel no es válido.')
else:
    print('Tu nivel de rendimiento es %s' % nivel)
    print('Tu salario es %.2f' % (bonificacion * puntos))

# 09. Escribir un programa para una empresa que quiere calcular el precio por entrar.
# Debe preguntar la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4
# y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input('Edad: '))
if edad < 4:
    precio = 0
elif edad >=4 and edad <= 18:
    precio = 5
else:
    precio = 10
print('Precio entrada: ', precio, '€')

# 10. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza son:
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte si quieres una pizza vegetariana o no,
# y muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza:\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Elige el ingrediente:\n\t1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Has elegido una pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Elige el ingrediente:\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Has elegido una pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")