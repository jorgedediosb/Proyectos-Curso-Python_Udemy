# Ejercicios lección 7 - MANEJO DE ERRORES

def pedirNumero():
    while True:
        #uso de excepciones parra evitar avisos de errores
        #puede usarse 'finally' para el el código haga algo con error o sin error, pero no se usa mucho
        try:
            numero = int(input("Escribe un nº: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Escribiste el número: {numero}")
            break
    print("Gracias")

pedirNumero()