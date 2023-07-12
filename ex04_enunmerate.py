#Ejercicios lección 4 - ENUMERATE (ENUMERADOR)

#enumerar el contenido de una colección
lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice, item)
    indice += 1
#hacemos lo mismo con menos líneas
lista = ['a','b','c']
for indice,item in enumerate(lista): #podemos indicar no sólo una lista sino cualquier cosa, tambien un range(x,y), por ejemplo
    print(indice,item)
#o los transformamos a tuples
lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)

programa = "Python"
lista_indices = list(enumerate(programa))
print(lista_indices)
# sirve tb para listas de strings:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
#o para enumerar los caracteres de un string:
lista_indices = "Python"
for indice,elemento in enumerate(lista_indices):
    print(indice,elemento)
    indice += 1
#Imprir índices y contenidos con alguna característica (empiecen con 'm')
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice,nombre)
        indice+=1
'''
lista_indices = list(enumerate(lista_nombres))
print(lista_indices)
'''
