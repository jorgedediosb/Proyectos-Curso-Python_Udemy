# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que pregunte al usuario por las ventas de un rango de años
# y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

import matplotlib.pyplot as plt
# Preguntamos por el año inicial
inicio = int(input('Introduce el año inicial: '))
# Preguntamos por el año final
fin = int(input('Introduce el año final: '))
# Definimos un diccionario vacío para guardar las ventas de cada año
ventas = {}
# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
# i toma como valores los años desde el año de inicio hasta el año final
for i in range(inicio, fin+1):
    # Preguntamos por las ventas del año i y las guardamos en el diccionario con la clave el año y el valor las ventas
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
# Definimos la figura y los ejes del gráfico con Matplotlib
fig, ax = plt.subplots()
# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(ventas.keys(), ventas.values())
# Mostarmos el gráfico por pantalla
plt.show()


# 02. Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso
# y una cadena con el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.

import matplotlib.pyplot as plt 

def diagrama_barras_notas(notas, color):
    '''Función que construye un diagrama de barras con las notas de las asignaturas de un curso.
    Parámetros:
        - notas: Es un diccionario formado por pares con clave el nombre de la asignaturay valor la nota.
        - color: Es una cadena con el color de las barras.
    Salida:
        - Un diagrama de barras con las notas del diccionario dado en el color dado.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las barras con las notas a partir del diccionario
    ax.bar(notas.keys(), notas.values(), color = color)
    # Devolvemos un objeto con los ejes y las barras que contienen
    return ax

notas = {'Programación':9, 'Mates':6.5, 'Economía':4, 'Historia': 8}
diagrama_barras_notas(notas, 'orange')
plt.show()


# 03. Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso
# y devuelva un diagrama de cajas con las notas. El diagrama debe tener el título “Distribución de notas”.

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_caja_notas(notas):
    '''Función que construye un diagrama de cajas con las notas de los alumnos de un curso.
    Parámetros:
        - notas: Es una serie de Pandas con las notas de los alumnos.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos los sectores con las verntas a partir de la serie
    notas.plot(kind = 'box', ax = ax)
    # Eliminamos las marcas del eje x 
    plt.xticks([])
    # 
    # Añadimos el título
    plt.title('Distribución de notas')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

notas = [4, 8, 7.5, 6, 5.5, 5.2, 3.5, 7.7, 3.2, 9, 6.8]
s_notas = pd.Series(notas)
diagrama_caja_notas(s_notas)
plt.show()


# 04. Escribir una función que reciba una serie de Pandas con el número de ventas de un
# producto durante los meses de un trimestre y un título y cree un diagrama de sectores
# con las ventas en formato png con el titulo dado. El diagrama debe guardarse en un fichero
# con formato png y el título dado.

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_sectores_ventas(ventas, titulo):
    '''Función que construye un diagrama de sectores con las ventas de un trimestre y lo guarda con un nombre dado. 
    
    Parámetros:
        - ventas: Es una serie de Pandas con las ventas del trimestre, siendo el índice los meses.
        - titulo: Es una cadena con el título.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos los sectores con las verntas a partir de la serie
    ventas.plot(kind = 'pie', ax = ax)
    # Eliminamos el título del eje y
    plt.ylabel('')
    # Añadimos el título
    plt.title(titulo)
    # Guardamos el gráfico con el nombre dado en formato png
    plt.savefig(titulo + '.png')
    return 

ventas = {'Enero':200, 'Febrero':240, 'Marzo':310}
s_ventas = pd.Series(ventas)
diagrama_sectores_ventas(s_ventas, 'Ventas primer trimestre')


# 05. Escribir una función que reciba una serie de Pandas con el número de ventas de un producto
# por años y una cadena con el tipo de gráfico a generar (lineas, barras, sectores, areas) y
# devuelva un diagrama del tipo indicado con la evolución de las ventas por años y con el título
# “Evolución del número de ventas”.

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_evolucion_ventas(ventas, tipo):
    '''Función que construye un diagrama del tipo indicado con la evolución de las ventas por años.
    
    Parámetros:
        - ventas: Es un dataframe de Pandas con las ventas, siendo el índice los años.
        - tipo: Es una cadena con el tipo de gráfico a dibujar: lineas, barras, sectores o areas.

    Salida:
        Un gráfico del tipo indicado con la evolución de las ventas.
    '''
    # Definimos un diccionario con los tipos de gráficos
    graficos = {'lineas':'line', 'barras':'bar', 'sectores':'pie', 'area':'area'}
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de líneas con los ingresos y los gastos
    ventas.plot(kind = graficos[tipo], ax = ax)
    # Añadimos el título
    plt.title('Evolución del número de ventas')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

df_ventas = pd.Series([1200, 840, 1325, 1280, 1500], index = [2000, 2001, 2002, 2003, 2004])
diagrama_evolucion_ventas(df_ventas, 'lineas')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'area')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'barras')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'sectores')
plt.show()


# 06. Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa
# por meses y devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos.
# El diagrama debe tener una leyenda identificando la línea de los ingresos y la de los gastos,
# un título con el nombre “Evolución de ingresos y gastos” y el eje y debe empezar en 0.

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_lineas_ingresos_gastos(datos):
    '''Función que construye un diagrama de lineas con los ingresos y gastos de un cuatrimestre.
    
    Parámetros:
        - datos: Es un dataframe de Pandas con dos columnas, una para los ingresos y otra para los gastos, y como índice los meses.

    Salida:
        Un gráfico de líneas con los ingresos y los gastos dados.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de líneas con los ingresos y los gastos
    datos.plot(ax = ax)
    # Añadimos la escala del eje y
    ax.set_ylim([0, max(datos.Ingresos.max(), datos.Gastos.max()) + 500])
    # Añadimos el título
    plt.title('Evolución de ingresos y gastos')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
df_datos = pd.DataFrame(datos).set_index('Mes')
diagrama_lineas_ingresos_gastos(df_datos)
plt.show()


# 07. El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con:
# Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa),
# Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante
# la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa).
# Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series
# temporales de las cotizaciones de cierre de cada banco.

import pandas as pd 
import matplotlib.pyplot as plt 

def evolucion_cotizacion(datos, variable):
    '''Función que construye un diagrama de lineas con la evolución de las cotizaciones de las empresas en bolsa.
    
    Parámetros:
        - datos: Es un dataframe de Pandas con las columnas Empresa, Apertura, Mínimo, Máximo, Cierre, Volumen.
        - variable: Es una cadena con el nombre de la columna del dataframe a dibujar.

    Salida:
        Un gráfico de líneas con las series temporales de las cotizaciones de cierre de cada empresa.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de cotizaciones por empresa
    datos.groupby('Empresa').plot(x = 'Fecha', y = variable, ax = ax)
    # Añadimos el título
    plt.title('Evolución de las cotizaciones (' + variable + ')')
    # Añadimos la legenda
    plt.legend(df_datos.groupby('Empresa').groups.keys())
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

# Creamos un dataframe a partir del fichero csv
df_datos = pd.read_csv('bancos.csv')
# Convertimos la columna Fecha a formato datetime
df_datos["Fecha"] = pd.to_datetime(df_datos["Fecha"])
# Llamamos a la función para crear el gráfico
evolucion_cotizacion(df_datos, 'Cierre')
plt.show()


# 08. El fichero titanic.csv contiene información sobre los pasajeros del Titanic.
# Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.
'''
1. Diagrama de sectores con los fallecidos y supervivientes.
2. Histograma con las edades.
3. Diagrama de barras con el número de personas en cada clase.
4. Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
5. Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
'''

import pandas as pd 
import matplotlib.pyplot as plt 

# Creamos un dataframe a partir del fichero csv
df_titanic = pd.read_csv('titanic.csv')
# Creamos la figura y los ejes
fig, ax = plt.subplots()
# Diagrama de sectores de falleccidos y supervivientes
df_titanic.Survived.value_counts().plot(kind = "pie", labels = ["Muertos", "Supervivientes"], title = "Distribución de supervivientes")
plt.show()

# Histograma de edades
df_titanic.Age.plot(kind = "hist", title = "Histograma de edades")
plt.show()

# Diagrama de barras con el número de personas de cada clase
df_titanic.Pclass.value_counts().plot(kind = "bar", title = "Número de personas por clase")
plt.show()

# Otra forma
df_titanic.groupby("Pclass").size().plot(kind = "bar", title = "Número de personas por clase")
plt.show()

# Diagrama de barras con el número de personas fallecidas y supervivientes de cada clase
df_titanic.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", title = "Número de personas fallecidas y supervivientes por clase")
plt.show()

# Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas de cada clase
df_titanic.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", stacked = True, title = "Número de personas fallecidas y supervivientes por clase")
plt.show()

