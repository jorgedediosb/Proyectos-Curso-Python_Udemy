#Ejercicios lección 3 - Métodos con listas, Diccionarios, tuples y sets

#type() nos dice el tipo de dato de una variable:
mi_lista = [1, "hola", 55, True, 5.76]
print(type(mi_lista))

#Agrega el elemento "motocicleta" a la siguiente lista:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta") #Método append() agrega elementos a la lista
print(medios_transporte)

#quitar el tercer elemento de la siguiente lista y almacenarlo en otra variable
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)

#DICCIONARIOS:
dic = {'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
print(type(dic))

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
#imprimimos el 2º elemento (e) de la 2ª clase (c2) y lo hacemos mayúscula
print(dic['c2'][1].upper())


mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#imprimimos '300':
print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
#cambiamos la edad:
mi_dic["edad"] = 36
#cambiamos la ocupación:
mi_dic["ocupacion"] = "Editora" 
#añadimos 'pais':
mi_dic["pais"] = "Colombia"

#TUPLAS
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
print(mi_tuple[2])

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
#count() dice cuantos elementos hay repetidos:
print(mi_tupla.count(2)) 

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
#Convertimos la tupla en una lista (o al revés):
mi_lista = list(mi_tupla)
print(type(mi_lista))

mi_tupla = (1, 2, 3, 4)
#Almacenamos los elementos de una tupla en varias variables distintas:
a,b,c,d = mi_tupla
print(a,b,c,d)

#SETS
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
#set1 y el set2 se une en un tercer set (set3) usando él método .union():
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)
#También se pueden unir con el operador |:
mi_set_3 = mi_set_1 | mi_set_2
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
#pop() elimina al azar un elemento del set:
print(sorteo.pop())

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
#add() añade un elemento al set:
sorteo.add("Damián") 
print(sorteo)

#BOLEANOS, devuelve el resultado booleano True o False
x = 5 == 6
x = 5 != 5
x = 5 < 7
x = 17834/34 > 87*56
x = bool(15 > 7)
print(x)

lista = [1,2,3,4]
#preguntamos si 5 está en la lista:
control = 5 not in lista
print(control) #=> False

#¿Es la raiz cuadrada de 25 igual a 5?
x = 25**0.5 == 5
print(x) # => True
