# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir una función que pida un número entero entre 1 y 10
# y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
# donde n es el número introducido.

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
# Opción 1:
f = open(nombre_fichero, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
# Opción 2:
with open(nombre_fichero, 'w') as f:
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')


# 02. Escribir una función que pida un número entero entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
# donde n es el número introducido, y la muestre por pantalla.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
# Opción 1:
try: 
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
    f.close()
# Opción 2:
try: 
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)


# 03. Escribir una función que pida dos números n y m entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
# y muestre la línea m del fichero. Si el fichero no existe debe informar de ello.

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
    print(lineas[m - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
    

# 04. Escribir un programa que acceda a un fichero de internet mediante su url
# y muestre por pantalla el número de palabras que contiene.

def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto
    y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    # Opción 1:
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())
    # Opción 2:
    try:
        with request.urlopen(url) as f:
            contenido = f.read()
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))


# 05. Escribir un programa que abra el fichero con información sobre el PIB per cápita
# de los países de la Unión Europea
# (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true),
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

# Opción 1:
def parsear_pib(url):
    '''
    Función que parsea un fichero con pibs de países.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
    Devuelve:
        Un diccionario con pares pais:pibs donde pibs es, a su vez, un diccionario con los años y los pibs del país.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista.
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        # Obtenemos los años de la primera linea del fichero.
        años = datos.pop(0).split('\t')[1:]
        # Creamos el diccionario prinpipal para guardar los pibs de todos los países.
        dict_pibs = {}
        # Bucle iterativo para recorrer las líneas del fichero.
        for pais in datos:
            datos_pais = pais.split('\t')
            # Obtenemos el código del país de los dos últimos caracteres del primer campo de la linea.
            codigo_pais = datos_pais.pop(0)[-2:]
            # Construimos un diccionario con los años y el pib del pais.
            dict_pais = {}
            # Bucle iterativo para recorrer los pibs del país.
            for i in range(len(datos_pais)):
                dict_pais[años[i].strip()] = datos_pais[i].strip()
            # Añadimos el diccionario con los pib del país al diccionario principal
            dict_pibs[codigo_pais] = dict_pais
        return dict_pibs

def pib(pibs, pais = "ES"):
    '''
    Función que recibe un diccionario con los pibs de los países y muestra por pantalla los pibs de un país dado.
    Parámetros:
        - pibs: Es un diccionario con los pibs de los países como el que devuelve la función parsear_pibs.
        - pais: Es una cadena con el código del país.

    Salida:
        Muestra por pantalla los pibs del país indicado.
    '''
    print("Año\tPIB")
    for i, j in pibs[pais].items():
        print(i, '\t', j)

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)


# Opción 2:
def pib_pais(url, pais = "ES"):
    '''
    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
        pais: Es una cadena con el código del país. 
    Devuelve:
        Un diccionario con pares año:pib del país dado que hay en el fichero con la url dada.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        datos = [i.split('\t') for i in datos] # Dividir cada línea por el tabulador
        datos = [list(map(str.strip, i)) for i in datos] # Eliminar espacios en blanco
        for i in datos:
            i[0] = i[0][-2:] # Obtener el código del país de los dos últimos caracteres del primer elemento de la lista
        datos[0][0] = 'años'
        # Creamos un diccionario con claves los códiogos de los países y valores la lista de sus pibs (a excepción del primer par que contiene los años).
        datos = {i[0]:i[1:] for i in datos}
        # Creamos y devolvemos el diccionario con los pibs del país
        return {datos['años'][i]:datos[pais][i] for i in range(len(datos['años']))}

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
print("Año\tPIB")
for i, j in pib_pais("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true", pais).items():
    print(i, '\t', j)


# 06. Escribir un programa para gestionar un listín telefónico con los nombres
# y los teléfonos de los clientes de una empresa.
# El programa incorporar funciones crear el fichero con el listín si no existe,
# para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente
# y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto
# listin.txt donde el nombre del cliente y su teléfono
# deben aparecer separados por comas y cada cliente en una línea distinta.

def get_phone(file, client):
    '''
    Función que devuelve el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
    '''
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            return directory[client]
        else:
            return('¡El cliente ' + client + ' no existe!\n')


def add_phone(file, client, telf):
    '''
    Función que añade el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
        telf: Es una cadena con el teléfono del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha añadido o ha habido algún problema.
    '''
    try: 
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(client + ',' + telf + '\n')
        f.close()
        return('El teléfono se ha añadido.\n')

def remove_phone(file, client):
    '''
    Función que elimina el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
    '''
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            del directory[client]
            f = open(file, 'w')
            for name, telf in directory.items():
                f.write(name + ',' + telf)
            f.close()
            return ('¡El cliente se ha borrado!\n')
        else:
            return('¡El cliente ' + client + ' no existe!\n')


def create_directory(file):
    '''
    Función que crea un fichero vacío para guardar un listín telefónico.
    Parámetros:
        file: Es un fichero.
    Devuelve:
        Un mesaje informando sobre si el fichero se ha creado correctamente o no.
    '''
    import os
    if os.path.isfile(file):
        answer = input('El fichero ' + file + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if answer == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    f = open(file, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'
     

def menu():
    '''
    Función que presenta un menú con las operaciones disponibles sobre un listín telefónico y devuelve la opción seleccionada por el usuario.
    Devuelve:
        La opción seleccionada por el usuario.
    '''
    print('Gesión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():
    '''
    Función que lanza la aplicación para la gestión del listín telefónico.
    '''
    file = 'listin.txt' 
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_phone(file, name))
        elif option == '4':
            print(create_directory(file))
        else:
            break
    return

directory()


# 07. El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35
# con las siguientes columnas:
# Nombre (nombre de la empresa),
# Final (precio de la acción al cierre de bolsa),
# Máximo (precio máximo de la acción durante la jornada),
# Mínimo (precio mínimo de la acción durante la jornada),
# Volumen (Volumen al cierre de bolsa),
# Efectivo (capitalización al cierre en miles de euros).

# 1. Construir una función reciba el fichero de cotizaciones
# y devuelva un diccionario con los datos del fichero por columnas.
# 2. Construir una función que reciba el diccionario devuelto por la función anterior
# y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.

def limpiar(cifra):
    """
    Función que elimina los puntos de separación de miles y cambia las comas de separación de decimales por puntos.
    Parámetros:
        - cifra: Es una cadena con una cifra
    Devuelve:
        Un real con la cifra de la cadena después de eliminar el separador de miles y cambiar el separador de decimales por punto.
    """
    cifra = cifra.replace('.', '')
    cifra = cifra.replace(',','.')
    return float(cifra) 

def preprocesado(ruta):
    """
    Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve un diccionario con los nombres de las columnas como claves y las listas de valores asociados a ellas.
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Un diccionario con pares formados por los nombres de las columnas y las listas de valores en las columnas.
    """
    try:
        # Abrimos el fichero en modo lectura
        with open(ruta, 'r') as f:
            # Leemos el fichero por líneas en una lista
            lineas = f.read().split('\n')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    
    # Leemos las claves del primer elemento de la lista y creamos una lista dividiendo la línea por el punto y coma.
    claves = lineas.pop(0).split(";")
    # Creamos el diccionario para guardar las cotizaciones
    cotizaciones = {}
    # Inicializamos el diccionario con listas vacías
    for i in claves:
        cotizaciones[i] = []
    # Bucle iterativo para recorrer la lista de lineas
    for linea in lineas:
        # Creamos una lista con los campos dividiendo la línea por el punto y coma
        campos = linea.split(';')
        # Añadimos el primer campo (el nombre de la empresa) a la lista del diccionario
        cotizaciones[claves[0]].append(campos[0])
        # Bucle iterativo para añadir el resto de los campos a las listas correspondientes del diccionario. 
        # Previamente los campos se limpian del carácter de separación de miles y se sustituye la coma por el punto para el separador de decimales.
        for i in range(1, len(campos)):
            cotizaciones[claves[i]].append(limpiar(campos[i]))
    return cotizaciones


def resumen_cotizacion(cotizaciones, ruta):
    """
    Función que recibe un diccionario con los valores de cotización y crear un fichero con un resumen con el mínimo, el máximo y la media.
    Parámetros:
        - cotizaciones: Es un diccionario con pares cuyas claves son los nombres de la variables medidas y cuyos valores son las listas de valores de cada variable.
        - ruta: Es una cadena con la ruta del fichero.
    """
    # Eliminamos el primer par del diccionario que contiene los nombres de las empresas.
    del(cotizaciones['Nombre'])
    # Inicializamos una cadena con el contenido que después se escribirá en el fichero.
    contenido = ""
    # Escribimos en la primera línea los nombres de las columnas.
    contenido += 'Nombre'
    # Bucle iterativo para crear los encabezados de las cotizaciones.
    for i in cotizaciones:
        contenido += ";" + i
    # Calculamos los mínimos de cada lista y los escribimos en las columnas correspondientes
    contenido += '\nMínimo'
    for i in cotizaciones.values():
        contenido += ';' + str(min(i))
    # Calculamos los máximos de cada lista y los escribimos en las columnas correspondientes
    contenido += '\nMáximo'
    for i in cotizaciones.values():
        contenido += ';' + str(max(i))
    # Calculamos las medias de cada lista y las escribimos en las columnas correspondientes
    contenido += '\nMedia'
    for i in cotizaciones.values():
        contenido += ';' + str(sum(i)/len(i))
    # Abrimos el fichero en modo escritura.
    with open(ruta, 'w') as f:
        # Escribimos el contenido en el fichero
        f.write(contenido)
    return


# Llamada a las funciones de prueba
cotizaciones = preprocesado('cotizacion.csv')
print(cotizaciones)
resumen_cotizacion(cotizaciones, 'resumen-cotizacion.csv')


# 08. El fichero calificaciones.csv contiene las calificaciones de un curso.
# Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
# Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final
# del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:
# Una función que reciba el fichero de calificaciones
# y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes
# y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
# Una función que reciba una lista de diccionarios como la que devuelve la función anterior
# y añada a cada diccionario un nuevo par con la nota final del curso.
# El peso de cada parcial de teoría en la nota final es de un 30%
# mientras que el peso del examen de prácticas es de un 40%.
# Una función que reciba una lista de diccionarios como la que devuelve la función anterior
# y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos.
# Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%,
# la nota de los exámenes parciales y de prácticas mayor o igual que 4
# y la nota final mayor o igual que 5.

def nota(cifra):
    '''Función que elimina cambia las comas de separación de decimales por puntos de una cifra y la convierte en un real.
    Parámetros:
        - cifra: Es una cadena con una cifra.
    Devuelve:
        Un real con la cifra de la cadena después de cambiar el separador de decimales por punto.
    '''
    cifra = cifra.replace(',','.')
    return float(cifra) 

def calificaciones(ruta):
    '''Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve una lista de diccionarios donde las claves de los diccionarios son los datos de la primera fila y los valores los datos de cada línea del fichero.
    
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Una lista de diccionarios donde cada diccionario contiene los datos de una linea del fichero (a excepción de la primera línea), usando como claves los datos de la primera línea.
    '''
    try:
        # Abrimos el fichero en modo lectura
        f = open(ruta, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    # Leemos el fichero por líneas en una lista
    lineas = f.readlines()
    # Cerramos el fichero
    f.close()
    # Leemos las claves del primer elemento de la lista, eliminamos el cambio de línea que aparece al final y dividimos la cadena por el punto y coma.
    claves = lineas[0][:-1].split(";")
    # Creamos la lista de calificaciones
    calificaciones = []
    # Recorremos las líneas del fichero y para cada línea creamos un diccionario que añadimos a la lista de calificaciones.
    for i in lineas[1:]:
        # Eliminamos el cambio de línea del final y dividimos la cadena por el punto y coma.
        valores = i[:-1].split(";")
        # Creamos un diccionario vacío para ir añadiendo los datos de cada alumno.
        alumno = {}
        # Recorremos la lista de valores y los añadimos al diccionario.
        for j in range(len(valores)):
            alumno[claves[j]] = valores[j]
        # Añadimos el diccionario a la lista de calificaciones
        calificaciones.append(alumno)
    return calificaciones

def añadir_nota_final(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, calcula la nota final del curso de cada alumno y la añade al diccionario del alumno.

    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        La lista de las calificaciones de los alumnos tras añadir a cada alumno de la lista su nota final del curso.
    '''

    def nota_final(alumno):
        '''Función que calcula la nota final del curso de un alumno.

        Parámetros:
            - alumno: Es un diccionario con las notas del alumno.
        Devuelve:
            El diccionario con los datos del alumno tras añadirle un nuevo par con la nota final del curso.
        '''
        if alumno['Ordinario1']: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
            parcial1 = nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1 = nota(alumno['Parcial1'])
        else: # No se ha presentado al primer parcial ni a la repesca en el ordinario
            parcial1 = 0
        if alumno['Ordinario2']: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
            parcial2 = nota(alumno['Ordinario2'])
        elif alumno['Parcial2']:
            parcial2 = nota(alumno['Parcial2'])
        else: # No se ha presentado al segundo parcial ni a la repesca en el ordinario
            parcial2 = 0 
        if alumno['OrdinarioPracticas']: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
            practicas = nota(alumno['OrdinarioPracticas'])
        elif alumno['Practicas']:
            practicas = nota(alumno['Practicas'])
        else:
            practicas = 0
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        return alumno

    # Aplicamos la función nota_final a todos los alumnos
    return list(map(nota_final, calificaciones))

def aprobados_suspensos(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, y devuelve la lista de aprobados y suspensos en el curso.

    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        - aprobados: Es una lista con los nombres de los alumnos aprobados.
        - suspensos: Es una lista con los nombres de los alumnos suspensos.
    '''
    # Creamos las listas de aprobados y suspensos vacías
    aprobados = []
    suspensos = []
    # Recorremos los alumnos del curso
    for alumno in calificaciones:
        # Si se cumplen las condiciones para aprobar añadimos el nombre del alumno a la lista de aprobados y si no a la de suspensos.
        if all([int(alumno['Asistencia'][:-1]) >= 75, alumno['Final1'] >= 4, alumno['Final2'] >=4, alumno['FinalPracticas'] >=4, alumno['NotaFinal'] >= 5]):
            aprobados.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
        else:
            suspensos.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
    return aprobados, suspensos

# Llamada a las funciones de prueba
print(añadir_nota_final(calificaciones('calificaciones.csv')))
aprobados, suspensos = aprobados_suspensos(añadir_nota_final(calificaciones('calificaciones.csv')))
print('Lista de aprobados:', aprobados)
print('Lista de suspensos:', suspensos)
