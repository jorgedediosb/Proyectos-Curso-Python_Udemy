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
        return f"La suma de tus dados es {suma_dados}. Ups, ¡tirada muy baja!"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. No está mal la tirada."
    else:
        return f"La suma de tus dados es {suma_dados}. ¡Buena tirada!"

continuar_juego = True
suma_total = 0

# Esperar al jugador para tirar los dados
while continuar_juego:
    input("Presiona Enter para tirar los dados...")
    # Lanzar los dados y obtener los valores
    dado1, dado2 = lanzar_dados()
    # Evaluar la jugada y imprimir el resultado
    resultado = evaluar_jugada(dado1, dado2)
    suma_total += dado1 + dado2
    print(resultado)
    print(f"La suma total hasta ahora es: {suma_total}")

    # Preguntar al jugador si quiere hacer otra tirada
    respuesta = input("¿Deseas hacer otra tirada? (s/n): ")
    if respuesta.lower() != "s":
        continuar_juego = False

print(f"La suma total de tus tiradas es: {suma_total}")