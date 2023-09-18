# Ejercicios lección 5 - INTERACCIÓN FUNCIONES "TIRAR DADOS"
# Crear función que arroje dos dados al azar y devuelva sus resultados:

# Función para lanzar los dados con resultados aleatorios
import random
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
 
# Función para evaluar el resultado
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"Tu tirada es de {suma_dados}. ¡Tirada baja!"
    elif suma_dados > 6 and suma_dados < 10:
        return f"Tu tirada es de {suma_dados}. Tirada media."
    else:
        return f"Tu tirada es de {suma_dados}. ¡Tirada alta!"

continuar_juego = True
suma_total = 0
valor_maximo = 21 # Valor máximo permitido

# Inicio juego
while continuar_juego and suma_total <= valor_maximo:
    input(f"Presiona 'Enter' para tirar los dados.\n¡No te pases de {valor_maximo}!")
    # Lanzar los dados y obtener los valores
    dado1, dado2 = lanzar_dados()
    # Evaluar la jugada e imprimir el resultado
    resultado = evaluar_jugada(dado1, dado2)
    suma_total += dado1 + dado2
    print(resultado)
    print(f"Dado 1: {dado1}\nDado 2: {dado2}")
    print(f"La suma total es: {suma_total}")

    if suma_total < valor_maximo:
        print(f"Te quedan {valor_maximo - suma_total} para pasarte.")
        respuesta = input("¿Deseas hacer otra tirada? (s/n): ")
        if respuesta.lower() != "s":
            continuar_juego = False

    elif suma_total > valor_maximo:
        print(f"OHHH Te has pasado de {valor_maximo} y has perdido!")
        continuar_juego = False
    
    else: # suma_total == valor_maximo
        print(f"¡BRAVO! Has sacado exactamente {valor_maximo} ")
        continuar_juego = False

print(f"La suma total de tus tiradas es: {suma_total}")