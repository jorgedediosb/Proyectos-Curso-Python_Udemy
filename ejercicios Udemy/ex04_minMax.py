# Ejercicios lección 4 - MIN MAX

#muestra el valor mínimo o máximo
menor = min(24,43,73,94,13)
mayor = max(24,43,73,94,13)
print(menor)
print(mayor)

lista = [24,43,73,94,13] #puede ser una lista de strings ['jorge','carlos','pepe']
print(min(lista))
print(max(lista))
print(f"El menor número de la lista es {min(lista)} y el número mayor es {max(lista)}")

nombre = 'jorge'
print(min(nombre)) # Primero coge mayúsculas y luego minúsculas

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)
diferencia = max(lista_numeros) - min(lista_numeros)
print(diferencia)

#con diccionarios
dic = {'C1':44, 'C2':11}
print(min(dic.values()))
print(min(dic))

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)