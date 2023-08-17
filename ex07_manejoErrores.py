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


def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")


def cociente(num1,num2):
    try:
        print(num1/num2)
#MENSAJE EN PANTALLA
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
#MENSAJES EN PANTALLA:
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")