# Ejercicios lección 6 - Manipular archivos

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