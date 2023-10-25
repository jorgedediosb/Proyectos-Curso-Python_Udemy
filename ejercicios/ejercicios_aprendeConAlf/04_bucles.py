# Ejercicios página https://aprendeconalf.es/docencia/python/ejercicios/

# 01. Escribir un programa que pida una palabra y la muestre por pantalla 10 veces.

palabra = input('Escribe una palabra y la repito x10: ')
for i in range(10):
    print(palabra)

# 02. Escribir un programa que la edad y muestre los años que ha cumplido (desde 1 hasta su edad).

edad = int(input('Edad: '))
for edad in range(1, edad + 1):
    print(edad)

# 03. Escribir un programa que pida un nº entero positivo
# y muestre todos los números impares desde 1 hasta ese número separados por comas.
number = int(input('Número: '))
output = ''
for i in range(1, number + 2, 2):
    if i < number:
        output += str(i) + ', '
    else:
        output += str(i) + '.'
print(output)

# 04. Escribir un programa que pida un nº entero positivo
# y muestre la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input('Número: '))
for i in range(number, -1, -1):
    print(i, end=',')


# 05. Escribir un programa que pregunte una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

amount = float(input("¿Cantidad a invertir?: "))
interest = float(input("¿Interés porcentual anual?: "))
years = int(input("¿Años?: "))
for i in range(years):
    amount *= (1 + interest) / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

# 06. Escribir un programa que pida al usuario un número entero y muestre un triángulo rectángulo con '*',
# de altura = al número introducido.

number = int(input('Altura del triángulo: '))
for i in range(number):
    for j in range(i+1):
        print('*', end='')
    print('')

# 07. Escribir un programa que muestre por pantalla la tabla de multiplicar de los nºs 1 al 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end='\t')
    print('')

# 08. Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable,
# pregunte por la contraseña hasta que introduzca la contraseña correcta.

clave_correcta = '1234'
clave_usuario = ''
while clave_usuario != clave_correcta:
    clave_usuario = input('Escribe la clave correcta: ')
print('Clave correcta!')

# 09. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# 10. Escribir un programa que pida una palabra y
# muestre una a una las letras de la palabra introducida empezando por la última.

palabra = input('Palabra: ')
for i in range(len(palabra)-1,-1,-1):
    print(palabra[i])

# 11. Escribir un programa que pida una frase y una letra,
# y muestre el número de veces que aparece la letra en la frase.

frase = input('Frase: ')
letra = input('Letra: ')
contador_letra = 0
for i in frase:
    if i == letra:
        contador_letra += 1
print("La letra '%s' se repite '%i' veces en la frase '%s'." %(letra, contador_letra, frase))

# 12. Escribir un programa que muestre el eco de todo lo que el usuario introduzca
# hasta que el usuario escriba “salir” que terminará.

while True:
    frase = input('Escribe algo o escribe "salir": ')
    if frase == 'salir':
        break
    print(frase)