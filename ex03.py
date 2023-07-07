#Ejercicios lección 3 - Método index()

palabra = "ordenador"
resultado = palabra.index("a")
print(resultado)

palabra = "atapuerca"
resultado = palabra.index("a",1,7) 
print(resultado) #el resultado es '2' porque desde la posición 1 (la 2ª) la 1ª 'a' está en la posición 2

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