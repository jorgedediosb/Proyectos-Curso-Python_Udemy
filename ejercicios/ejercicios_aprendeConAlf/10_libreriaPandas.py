# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que pregunte al usuario por las ventas de un rango de años
# y muestre una serie con los datos de las ventas indexada por los años,
# antes y después de aplicarles un descuento del 10%.

import pandas as pd

inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {}
for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) + ': '))
# creamos un objeto de clase 'pd.Series' a partir del diccionario 'ventas' para acceder a ellos.
ventas = pd.Series(ventas)
print('Ventas SIN descuento:\n', ventas)
print('-----------------------')
print('Ventas CON descuento:\n', ventas*0.9)


# 02. Escribir una función que reciba un diccionario con las notas de los alumnos de un curso
# y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

# import pandas as pd
def estadistica_notas(notas):
    """
    Calcula estadísticas básicas de un diccionario de notas.
    Parámetros:
    notas (dict_dic): Diccionario con nombres de estudiantes (claves) y calificaciones (valores).
    Devuelve:
    pd.Series: objeto Serie de Pandas con estadísticas.
    """
    notas = pd.Series(notas)
    # Opción 1:
    estadisticas = pd.Series([notas.min(),
                              notas.max(),
                              notas.mean(),
                              notas.std()],
                              index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticas
    '''
    Opción 2 usando .describe() que ofrece los datos pedidos y alguno más:
    def estadistica_notas(notas):
        notas = pd.Series(notas)
        return notas.describe()
    
    Opción 3 redondeando los resultados a 2 decimales e imprimiendo el nombre de alumno con su nota(min y max):
    def estadistica_notas(notas):
        notas = pd.Series(notas)
        # Calcular las estadísticas
        min_nota = notas.idxmin()
        max_nota = notas.idxmax()
        mean = round(notas.mean(), 2)
        std = round(notas.std(), 2)

        # Crear una cadena de texto formateada con las estadísticas
        estadisticas = f"min: {notas[min_nota]} - {min_nota}\nmax: {notas[max_nota]} - {max_nota}\nmean: {mean}\nstd: {std}"
        return estadisticas
    '''
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))


# 03. Escribir una función que reciba un diccionario con las notas de los alumnos de un curso
# y devuelva una serie con las notas de los alumnos APROBADOS (notas >= 5)
# y ordenadas de mayor a menor.

import pandas as pd

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)

notas = {'Juan':7.5, 'María':3.5, 'Pedro':4, 'Carmen': 5, 'Luis': 9.5}
print(aprobados(notas))


# 04. Escribir programa que genere y muestre por pantalla un DataFrame
# con los datos de la tabla siguiente:
# Mes	  Ventas  Gastos
# Enero	  30500	  22000
# Feb     35600	  23400
# Marzo	  28300	  18100
# Abril	  33900	  20700

# import pandas as pd
# Opción 1 con un dic:
datos1 = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
          'Ventas':[30500, 35600, 28300, 33900],
          'Gastos':[22000, 23400, 18100, 20700]}
contabilidad = pd.DataFrame(datos1)
print(contabilidad)

# Opción 2 con una lista:
datos2 = [['Enero', 30500, 22000],
          ['Febrero', 35600, 23400],
          ['Marzo', 28300, 18100],
          ['Abril', 33900,20700]]
contabilidad = pd.DataFrame(datos2, columns=['Mes', 'Ventas', 'Gastos'])
print(contabilidad)


# 05. Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
# una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
         'Ventas':[30500, 35600, 28300, 33900],
         'Gastos':[22000, 23400, 18100, 20700]}

contabilidad = pd.DataFrame(datos)

# Opción 1 usando los datos1 ej anterior:
def balance1(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    # Se filtra el DataFrame 'contabilidad'
    # para incluir solo las filas cuyo valor en la columna 'Mes' esté en la lista 'meses'.
    # Luego, se selecciona la columna 'Balance' y se suma para calcular el balance total de esos meses.
    # El resultado se devuelve como el valor de retorno de la función balance1.
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

print(balance1(contabilidad, ['Enero','Marzo']))

# Opción 2 usando los datos2 ej anterior:
def balance2(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    # Se establece el índice del DataFrame en la columna 'Mes' utilizando set_index.
    # Luego, se utiliza loc para seleccionar las filas correspondientes a los meses en la lista 'meses',
    # la columna 'Balance' y se suma para calcular el balance total de esos meses.
    return contabilidad.set_index('Mes').loc[meses,'Balance'].sum()

print(balance2(contabilidad, ['Enero','Abril']))

# 06. El fichero cotizacion.csv (https://github.com/asalber/aprendeconalf/blob/master/content/es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv)
# contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
# nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa),
# Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada),
# volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
# Construir una función que construya un DataFrame a partir del un fichero con el formato anterior
# y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

# import pandas as pd
def resumen_cotizaciones(archivo):
    df = pd.read_csv(archivo, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

print(resumen_cotizaciones('dataSets/cotizacion.csv'))

# 07. El fichero titanic.csv contiene información sobre los pasajeros del Titanic.
# Escribir un programa con los siguientes requisitos:
'''
1. Generar un DataFrame con los datos del fichero.
2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
3. Mostrar por pantalla los datos del pasajero con identificador 148.
4. Mostrar por pantalla las filas pares del DataFrame.
5. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
8. Eliminar del DataFrame los pasajeros con edad desconocida.
9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
10. Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
11. Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
'''
# import pandas as pd
# Generar un DataFrame con los datos del fichero.
titanic = pd.read_csv('dataSets/titanic.csv', index_col=0)
print(titanic)

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas
# y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
print('Dimensiones:', titanic.shape)
print('Número de elemntos:', titanic.size)
print('Nombres de columnas:', titanic.columns)
print('Nombres de filas:', titanic.index)
print('Tipos de datos:\n', titanic.dtypes)
print('Primeras 10 filas:\n', titanic.head(10))
print('Últimas 10 filas:\n', titanic.tail(10))

# Mostrar por pantalla los datos del pasajero con identificador 148
print(titanic.loc[148])

# Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(0,titanic.shape[0],2)])

# Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())

# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)
# Alternativa
# print(titanic['Survived'].value_counts(normalize=True) * 100)

#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))
# Alternativa con % y dos dígitos:
# result = titanic.groupby('Pclass')['Survived'].value_counts(normalize=True).apply(lambda x: f'{x * 100:.2f} %')
# print(result)

# Eliminar del DataFrame los pasajeros con edad desconocida.
titanic.dropna(subset=['Age'])
# Alternativa 
# titanic = titanic[titanic['Age'].notna()]

# Mostrar la edad media de las mujeres que viajaban en cada clase.
print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic['Young'] = titanic['Age'] < 18

# Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(titanic.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)


# 08. Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv,
# contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019
# respectivamente. Escribir un programa con los siguientes requisitos:
'''
1. Generar un DataFrame con los datos de los cuatro ficheros.
2. Filtrar las columnas del DataFrame para quedarse con las columnas
ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
3. Reestructurar el DataFrame para que los valores de los contaminantes de las
columnas de los días aparezcan en una única columna.
4. Añadir una columna con la fecha a partir de la concatenación del año, el mes
y el día (usar el módulo datetime).
5. Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy)
y ordenar el DataFrame por estaciones contaminantes y fecha.
6. Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
7. Crear una función que reciba una estación, un contaminante y un rango de fechas
y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
8. Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
9. Mostrar un resumen descriptivo para cada contaminante por distritos.
10. Crear una función que reciba una estación y un contaminante y devuelva un resumen
descriptivo de las emisiones del contaminante indicado en la estación indicada.
11. Crear una función que devuelva las emisiones medias mensuales de un contaminante
y un año dados para todos las estaciones.
12. Crear un función que reciba una estación de medición y devuelva un DataFrame con
las medias mensuales de los distintos tipos de contaminantes.
'''
import pandas as pd
import numpy as np
import datetime as dt

# Generar un DataFrame con los datos de los cuatro ficheros
emisiones_2016 = pd.read_csv('emisiones-2016.csv', sep = ';')
emisiones_2017 = pd.read_csv('emisiones-2017.csv', sep = ';')
emisiones_2018 = pd.read_csv('emisiones-2018.csv', sep = ';')
emisiones_2019 = pd.read_csv('emisiones-2019.csv', sep = ';')
emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])
emisiones

# Filtrar las columnas del DataFrame para quedarse con las columnas
# ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc. 
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([col for col in emisiones if col.startswith('D')])
emisiones = emisiones[columnas]
emisiones

# Reestructurar el DataFrame para que los valores de los contaminantes
# de las columnas de los días aparezcan en una única columna.
emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
emisiones

# Crear una nueva columna con las fechas a partir del año, mes y día
# Primero eliminamos el caracter D del comienzo de la columna de los días
emisiones['DIA'] = emisiones.DIA.str.strip('D')
# Concatenamos las columnas del año, mes y día
emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.apply(str)
# Convertimos la nueva columna al tipo fecha
emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')
emisiones

# Eliminar las filas con fechas no válidas
emisiones = emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)
# Ordenar el el dataframe por estación, magnitud y fecha
emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])

# Mostrar las estaciones disponibles
print('Estaciones:', emisiones.ESTACION.unique())
# Mostrar los contaminantes disponibles
print('Contaminantes:', emisiones.MAGNITUD.unique())

# Función que devuelve las emisiones de un contaminante dado en una estación y rango de fechas dado.
def evolucion(estacion, contaminante, desde, hasta):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)
                     & (emisiones.FECHA >= desde) & (emisiones.FECHA <= hasta)].sort_values('FECHA').VALOR
evolucion(56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d'))

# Resumen descriptivo por contaminantes
emisiones.groupby('MAGNITUD').VALOR.describe()

# Resumen descriptivo por contaminantes y distritos
emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()

# Función que devuelve un resumen descriptivo de la emisiones en un contaminante dado en un estación dada
def resumen(estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()

# Resumen de Dióxido de Nitrógeno en Plaza Elíptica
print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', resumen(56, 8),'\n', sep='')
# Resumen de Dióxido de Nitrógeno en Plaza del Carmen
print('Resumen Dióxido de Nitrógeno en Plaza del Carmen:\n', resumen(35, 8), sep='')

# Función que devuelve una serie con las emisiones medias mensuales de un contaminante
# y un mes año para todos las estaciones
def evolucion_mensual(contaminante, año):
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')

# Evolución del dióxido de nitrógeno en 2019
evolucion_mensual(8, 2019)
