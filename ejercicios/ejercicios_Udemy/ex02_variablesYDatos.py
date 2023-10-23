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
print(type(num_entero)) #type imprime el tipo de dato

num_decimal = 23.23 #los float van con punto, no con coma
print(type(num_decimal))

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))

#conversión explícita de float a int
num1 = 7.5
num1 = int(num1) #convertimos el float 7.5 a un int (7)
print(num1)
print(type(num1))

#conversión implícita de int a float
num2 = 10
num2 = 10 + 0.5 #si sumamos a un entero un float, se transformará a float
print(num2)
print(type(num2))

#conversión explícita de int a float
num3 = 1000
print(num3, "es un entero")
num3 = float(num3)
print(num3, "pero ahora es lo transformo!")
print("y ahora es: ", type(num3))

num1 = "7.5"
num2 = "10"
print("concatenamos", num1 + num2) #Al ser strings, los contatena, no los suma
print("Transformánsolos la suma es: ", float(num1) + int(num2)) #los convertimos a float e int para poder sumarlos

#Uso de .format ({}) para contatenar strings
x = 7
y = 3
z = x + y #podemos crear otras variables para la suma, pero no es necesario
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
print(round(10/3, 2)) #redondeamos la división 10/3 dejando únicamente 2 decimales

valor = 10.676767
print(round(valor)) #redondeamos el valor a su entero más cercano (11)
print(round(5**0.5, 4)) #Raiz cuadrada de 5 dejando el resultado en 4 decimales