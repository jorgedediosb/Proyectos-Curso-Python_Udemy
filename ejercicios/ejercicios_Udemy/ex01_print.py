# Ejercicios curso Python Udemy - Lección 1 - print y input

# Uso de print para imprimir texto usando '' y ""
print('Estudiar con "Python Total" es genial')

# Uso de print con saltos de línea (\n):
print('Línea 1\nLínea 2\nLínea 3')

# Uso de print + 'sep' y 'end'
print('Termino esta frase con punto', end=".\n") #hay que indicar el salto de línea \n
print(1,2,3)
print(1,2,3, sep=",")
print(1,2,3, sep=",", end='.\n')

# Uso de print con tabulaciones (\t) y saltos de línea (\n):
print('A\tB\tC\nD\tE\tF\nG\tH\tI')

print('\tBarra Normal: /\n\tBarra Invertida: \\')

# Uso de print + input
print("Estás estudiando: " + input("¿Qué estás estudiando?: "))

print("Tu nombre es: " + input("Escribe tu nombre: ") + " " + input("Escribe tu apellido: "))

