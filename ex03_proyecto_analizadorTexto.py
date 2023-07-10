texto = input("Ingresa el texto que quieras analizar: ")
letras = []

#Transformamos todo el texto en minúsculas para que quede igualado
texto = texto.lower()

#La letra que introducimos en el input la añadimos a la variable 'letras' con el método append()
#La letra la transformamos a minúscula para se busque en el texto que tb se transformó en minúscula
letras.append(input("Primera letra o símbolo que quieres buscar: ").lower())
letras.append(input("Segunda letra o símbolo que quieres buscar: ").lower())
letras.append(input("Tercera letra o símbolo que quieres buscar: ").lower())
print("\n")

#Contamos las veces que se repite en el texto la letra que se ha introducido (almacenada en la variable letra)
#Como introducimos en la variable 3 letras, 1º buscamos la posición 0, luego la 1 y luego la 2.
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se ha encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces.")
print(f"Se ha encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces.")
print(f"Se ha encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces.")
print("\n")
      
#Contamos las palabras del texto usando split() que separa el texto en palabras (separadas por espacios)
#Contamos las palabras almacenadas en la lista 'palabras' con len()
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto.")
print("\n")

#Seleccino el primer y último carácter del texto para mostrar la primera y última letra
print("LETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La primera letra de tu texto es '{letra_inicio}' y la última es '{letra_final}'.")
print("\n")

#uso reverse para invertir las palabras
#join para volver a unirlas
print("TEXTO INVERTIDO")
palabras_invertidas = palabras[::-1] #Invierte el orden de las palabras
texto_invertido = ' '.join([palabras[::-1] for palabras in palabras_invertidas]) #Invierte cada caracter de cada palabra y las une en un texto
print(f"Tu texto invertido sería este:\n '{texto_invertido}'")
print("\n")

#creo un diccionario con True y False para que me indique si existe la palabra Python en el texto
print("BUSCAR PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"SI", False:"NO"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")