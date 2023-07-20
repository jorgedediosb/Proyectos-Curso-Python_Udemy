# Ejercicios lección 6 - Manipular archivos

# Imprimir un texto
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