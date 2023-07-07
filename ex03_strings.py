#Ejercicios lección 3 - Métodos con Strings

# Método index()
palabra = "ordenador"
resultado = palabra.index("a")
print(resultado)

palabra = "atapuerca"
resultado = palabra.index("a",1,7) 
print(resultado) #el resultado es '2' porque desde la posición 1 (la 2ª) la 1ª 'a' está en la posición 2

#Extraer cadenas de texto
palabra = "ordenador"
quinto_caracter = palabra[4]  # Índice 4 representa la quinta posición (empezando desde 0)
print("El quinto carácter de la palabra 'ordenador' es:", quinto_caracter)

#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica",0,100)
print(resultado) #resultado es 26 xq "práctica" empieza en ese ínice

#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" 
frase = "En teoría, la práctica es buena práctica"
resultado = frase.rindex("práctica", 0, 100) #Usando rindex, empezamos la búsqueda desde el final, de izq a der.
print(resultado) #Resultado: 32. Es donde empieza la última aparición de "práctica"

#Extraer cadenas de texto (sub-strings) o slicing
texto = "pepito"
resultado = texto[2:5] #desde el índice 2 hasta el índice 5
print(resultado)

texto = "pepito"
resultado = texto[2:] #desde el índice 2 hasta el final
print(resultado)

texto = "atapuerca"
resultado = texto[0:5:2] #desde el índice 0 hasta el índice 5, salatándose 2 cada vez
print(resultado)

texto = "atapuerca"
resultado = texto[::2] #desde el índice 0 hasta el final, salatándose 2 cada vez
print(resultado)

texto = "atapuerca"
resultado = texto[::-1] #desde el índice 0 hasta el final, salatándose 2 cada vez
print(resultado)

#Otros métodos para trabajar con strings:
texto = "abracadabra"
resultado = texto.upper() #transforma en mayúsculas. Con lower() transformamos en minúsculas
print(resultado)

frase = "Hola qué tal"
resultado = frase.split() #separamos en distintas palabras a partir del espacio. Podemos indicar frase.split(" ",2) para indicar que se separen con comillas y sólo haya 2 conjuntos
print(resultado)

lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras) #unimos la lista en un sólo string, indicando como queremos juntar cada elemento
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.find("difícil") #Buscamos palabras. Funciona como index() pero si no encuentra nada devuelve -1
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil", "fácil").replace("mala", "buena") #Reemplazamos distintas palabras
print(resultado)

#propiedades de los strings

#Concatenable (suma) o multiplicable:
palabra = "Repetición"
print(palabra*15)

#Buscar partes del string (usando ''' ponemos los saltos de línea directamente, sin \n)
poema = '''Tierra mojada
mis recuerdos de viaje,
entre las lluvias'''
print("agua" not in poema)

palabra = "electroencefalografista"
print(len(palabra)) # Longitud del string