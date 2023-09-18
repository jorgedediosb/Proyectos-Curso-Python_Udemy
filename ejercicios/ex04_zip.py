# Ejercicios lección 4 - ZIP

# Zip combina 2 o más listas entrelazando sus elementos en tuplas
nombres = ['Elena','Jorge','Oscar']
edades = [36,43,45]
ciudades = ['Arévalo','Madrid','Ávila']
listado = list(zip(nombres,edades, ciudades))
for nombres,edades,ciudades in listado:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}.")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
frase = list(zip(capitales,paises))
for capitales,paises in frase:
    print(f"La capital de {paises} es {capitales}")

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
numeros = list(zip(espaniol, portugues, ingles))
print(numeros)

# Se puede crear un sólo elemento 'zip':
marcas = ['nike','danone','apple']
productos = ['zapatillas','yogur','ordenador']
mi_zip = zip(marcas,productos) # Si lo metemos dentro de una lista se imprimirá:list(zip(marcas,productos))
print(mi_zip)