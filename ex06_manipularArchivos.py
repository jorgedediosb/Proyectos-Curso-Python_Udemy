# Ejercicios lección 6 - Manipular archivos + Mçetodo Path

# Imprimir un texto creado en la misma carpeta del archivo original.py (por eso no se indica una ruta)
mi_texto = open('texto.txt') #debemos meter el archivo en una variable para abrirla
print(mi_texto.read()) #una vez abierto el archivo hay que leerlo
mi_texto.close() #conviene indicar close() para reservar espacio de memoria

# Imprimir la primera línea
mi_texto = open('texto.txt')
print(mi_texto.readline()) #con readline() leemos la primera línea
mi_texto.close()

# Imprimir líneas sueltas
mi_texto = open('texto.txt')
todas = mi_texto.readlines() #nueva variable para hacer una lista con todas las líneas usando .readlines()
print(todas[1]) #se imprime sólo la 2ª línea
mi_texto.close()

# Crear archivos
# open() Puede recibir los parámetros 'r' (read o leer),
# 'w' (write o sobreescribir),
# 'a' (escribe el nuevo contenido después del que ya hay)

# con 'w' se sorbreescribe el texto original por el nuevo
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

# con 'a' se imprime el nuevo texto al final del que ya había
archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

# Uso del método writelines para escribir los valores en una lista al final del archivo "registro.txt"
# Se inserta un tabulador entre cada elemento de la lista para separarlos.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
registro = open('registro.txt','a')
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')
registro.close()
registro = open('registro.txt','r')
print(registro.read())

# MÉTODO PATH

# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
from pathlib import Path
ruta_base = Path.home()

# crea una ruta relativa que nos permita llegar al archivo "practicas_path.py"
# a partir de la siguiente estructura de carpetas: 
# Curso Pytho > Día 6 > practicas_path.py 
# 3# Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
from pathlib import Path
ruta = Path("Curso Python/Día 6/practicas_path.py")

# Igual, pero con una ruta absoluta que permita llegar al archivo "practicas_path.py"
from pathlib import Path
ruta_base = Path.home()
ruta = ruta_base / "Curso Python" / "Día 6" / "practicas_path.py"

# FUNCIONES
# Función que abre un archivo como parámetro, y devuelva su contenido.
def abrir_archivo(nombre_archivo):
    contenido = ''
    archivo = open(nombre_archivo,'r')
    contenido = archivo.read()
    archivo.close()
    return contenido
# Ejemplo de uso
nombre_archivo = "archivo.txt"
contenido_archivo = abrir_leer(nombre_archivo)
print(contenido_archivo)


# Crea una función que abra un archivo indicado como parámetro,
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo,'w')
    archivo.write("contenido eliminado")
    archivo.close()
    return "Contenido sobrescrito exitosamente."
# Ejemplo de uso
nombre_archivo = "archivo.txt"
resultado = sobrescribir(nombre_archivo)
print(resultado)


# Función que abre un archivo indicado como parámetro,
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
# Finalmente, cierra el archivo abierto.

def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, 'a')
    archivo.write("Se ha registrado un error de ejecución\n")
    archivo.close()
    return "Error registrado exitosamente."
# Ejemplo de uso
nombre_archivo = "registro.txt"
resultado = registro_error(nombre_archivo)
print(resultado)