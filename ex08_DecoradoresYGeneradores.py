# Ejercicios lección 8 - DECORADORES Y GENERADORES

# DECORADORES
# Modifican funciones sin duplicar código
def mostrar_info(function):
    def interior():
        print(f'Ejecutando función {function.__name__}')
        function()
        print('Ejecución finalizada')
    return interior
def impresion():
    print('Hola mundo')
funcion_decorada = mostrar_info(impresion)
funcion_decorada()

# GENERADORES
# 'Demoran' iteraciones hasta que se solicitan

# Función con números infinitos a partir de 1
def infinito():
    num = 0
    while True:
        yield num #usan yield en vez de return
        num += 1

generador = infinito()
print(next(generador))

# Función múltiplos de 7 infinitos
def multiploSiete():
    num = 1
    while True:
        yield num*7
        num += 1

generador = multiploSiete()

# Función que envía mensaje cada vez que se pierde una vida hasta 'game over'
def mensaje_vidas():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x

perder_vida = mensaje_vidas()