# Ejercicios lección 5 - ARGUMENTOS

# Función que tome una cantidad indeterminada de argumentos numéricos,
# y que retorne la suma de sus valores al cuadrado.
def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += num*+2
    return suma
print(suma_cuadrados(2,3,6))

# Función que tome un conjunto de argumentos de cualquier extensión,
# y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume,
# o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
def suma_absolutos(*args):
    suma = 0
    for num in args:
        suma += abs(num)
    return suma
resultado = suma_absolutos(-1,2,-4,5)
print(resultado)

# Función que reciba, como primer argumento, un nombre,
# y a continuación, una cantidad indefinida de números.
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje
resultado = numeros_persona("Juan", 1, 2, 3, 4)
print(resultado)  # Juan, la suma de tus números es 10

# Uso de **kwargs y *args (y otros argumentos)
def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100, 200, 300]
kwargs = {'a':10, 'b':20, 'c':30}

prueba(15, 50, *args, **kwargs)

# Función que cuente la cantidad de parémetros que se entregan,
# y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

# Función que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords).
# La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

# Funcioón que tome como parámetros su nombre y luego una cantidad indetermida de argumentos.
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')