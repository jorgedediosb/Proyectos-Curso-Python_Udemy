# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que guarde en una variable el diccionario:
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte por una divisa y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
simbolo_divisas = input("Introduce una divisa y te doy su símbolo: ")
# Opción 1:
if simbolo_divisas.title() in divisas:
    print(f"El símbolo del {simbolo_divisas} es: {divisas[simbolo_divisas.title()]}")
else:
    print("La divisa no existe")
# Opción 2:
print(divisas.get(simbolo_divisas.title(), "La divisa no está."))


# 02. Escribir un programa que pregunte al usuario su nombre, edad y teléfono
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje:
# <nombre> tiene <edad> años y su número de teléfono es <teléfono>.

nombre = input("Nombre: ")
edad = input("Edad: ")
telefono = input("Telefono: ")
persona = {'Nombre' : nombre, 'Edad' : edad, 'Teléfono' : telefono}
print(f"{persona['Nombre']} tiene {persona['Edad']} años y su teléfono es {persona['Teléfono']}")


# 03. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y
# muestre el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else:
    print("Lo siento, la fruta", fruta, "no está disponible.")


# 04. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
# muestre la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio',
         8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])


# 05. Escribir un programa que almacene el diccionario con las asignaturas de un curso:
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y muestre por pantalla
# los créditos de cada asignatura en formato: <asignatura> tiene <créditos> créditos,
# Al final debe mostrar también el número total de créditos del curso.

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
TOTAL_CREDITOS = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    TOTAL_CREDITOS += creditos
print('Número total de créditos del curso: ', TOTAL_CREDITOS)


# 06. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una persona (nombre, edad, sexo, teléfono, etc.) que se le pida al usuario.
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}
CONTINUAR = True
while CONTINUAR:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    CONTINUAR = input('¿Quieres añadir más información (Si/No)? ') == "Si"

# 07. Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. Después se debe mostrar la lista de la compra
# y el coste total, con el formato: <Artírulo 1> <precio> y el total al final.

cesta = {}
CONTINUAR = True
while CONTINUAR:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    CONTINUAR = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
COSTE = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    COSTE += precio
print('Coste total: ', COSTE)

# 08. Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario = {}
palabras = input("""Introduce la lista de palabras y traducciones
                 en formato palabra:traducción separadas por comas: """)
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')


# 09. Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será
# el número de factura y el valor el coste de la factura.
# El programa debe preguntar si quiere añadir una nueva factura, pagar una existente o terminar.
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste
# y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura
# y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla
# la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas = {}
COBRADO = 0
PENDIENTE = 0
MORE = ''
while MORE != 'T':
    if MORE == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        PENDIENTE += coste
    if MORE == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        COBRADO += coste
        PENDIENTE -= coste
    print('Recaudado:', COBRADO)
    print('Pendiente de cobro: ', PENDIENTE)
    MORE = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')


# 10. Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
# y el valor será otro diccionario con los datos (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:

# 1. Preguntar los datos, crear un diccionario con los datos y añadirlo a la base de datos.
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3. Preguntar por el NIF del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6. Terminar el programa.

clientes = {}
OPCION = ''
while OPCION != '6':
    if OPCION == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if OPCION == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if OPCION == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if OPCION == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if OPCION == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input("""Menú de opciones\n(1) Añadir cliente\n(2)
                   Eliminar cliente\n(3)
                   Mostrar cliente\n(4) Listar clientes\n(5)
                   Listar clientes preferentes\n(6)
                   Terminar\nElige una opción:""")


# 11. El directorio de los clientes de una empresa está organizado en una cadena de texto:
# "nif;nombre;email;teléfono;descuento\n
# 01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n
# 71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n
# 63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n
# 98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento.
# Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene
# los nombres de los campos con la información contenida en el directorio.
# Escribir un programa que genere un diccionario con la información del directorio,
# donde cada elemento corresponda a un cliente y tenga por clave su nif
# y por valor otro diccionario con el resto de la información del cliente.
# Los diccionarios con la información de cada cliente tendrán como claves los nombres
# de los campos y como valores la información de cada cliente correspondientes a los campos.
# Es decir, un diccionario como el siguiente

# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';')
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # información del cliente
    lista_info = i.split(';')
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal
    for j in range(1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)
