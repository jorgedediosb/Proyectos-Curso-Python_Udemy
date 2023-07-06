#Ejercicios curso Python Udemy - Lección 2 - Variables y tipos de datos

nombre = "Tony Soprano"
edad = "51"
print(nombre + edad)

nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print(nombrecompleto)

curso = "Python"
print("Estás tomando un curso de " + curso)

num_entero = 10
print(type(num_entero)) #Type imprime el tipo de dato

num_decimal = 23.23 #los float van con punto, no con coma
print(type(num_decimal))

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))

num1 = 7.5 #conversión explícita de float a int
num1 = int(num1) #hacemos que el float 7.5 sea un int (7)
print(num1)
print(type(num1))

num2 = 10 #conversión implícita de int a float
num2 = 10 + 0.5 #hacemos que el int 10 sea un float (10.5)
print(num2)
print(type(num2))

num1 = "7.5"
num2 = "10"
print(num1 + num2) #Al ser strings, los contatena, no los suma
print(float(num1) + int(num2)) #los convertimos a float y int para poder sumarlos

#Uso de .format para contatenar string
x = 7
y = 3
z = x + y #podemos crear otras variable para la suma, pero no es necesario
print("La suma de " + str(x) + " y " + str(y) + " es " + str(x + y)) #sin .format
print("La suma de {} y {} es {}".format(x, y, x+y)) #usando .format
print(f"La suma de {x} y {y} es {x+y}") #usando cadenas literales (f)
print(f"La división de {x} y {y} es {x/y}") #usando cadenas literales (f)
print(f"La división 'al piso' de {x} y {y} es {x//y}")
print(f"La división 'al piso' de {x} y {y} es {int(x/y)}") #convirtiendo el resultado en número entero
print(f"{x} elevado a {y} es {x**y}") #Potencias
print(f"{x} elevado a {10} es {x**10}") #Potencias
print(f"La raiz cuadrada de {x} es {x**0.5}") #Raiz Cuadrada

#uso de round para redondear
print(round(10/3, 2)) #redondeamos la división 10/3 dejando únnicamente 2 decimales
valor = 10.676767
print(round(valor)) #redondeamos el valor a su entero más cercano (11)
print(round(5**0.5, 4)) #Raiz cuadrada de 5 dejando el resultado en 4 decimales