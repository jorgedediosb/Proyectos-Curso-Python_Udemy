# Ejercicios lección 5 - MÉTODOS / FUNCIONES

# Existen decenas de métodos/funciones. Documentación en python.orgs
dic = {"clave1":"valor1", 'clace2':'valor2'}
print(dic)
dic.popitem()
print(dic)
dic.clear()
print(dic)

# Elimina caracteres con lstrip()
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

# Inserta elemenntos con insert()
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

# Verificar conjuntos aislados (nada en común) con isdisjoint() 
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

# Podemos crear nuestras propias funciones:
def saludar(nombre):
    print("hola " + nombre)
saludar('Jorge')

def cuadrado(un_numero):
    print(un_numero**2)
un_numero = 4
cuadrado(un_numero)

# Uso de 'return'. No imprime nada pero devuelve valores que los podemos almacenar en variables
def sumar(a,b):
    return a+b
resultado = sumar(10,20)
print(resultado)

def potencia(base,exponente):
    return base**exponente
resultado = potencia(3,5)
print(resultado)

def usd_a_eur(valor):
    return valor*0.90
dolares = usd_a_eur(100)
print(dolares)

def invertir_palabra(palabra):
    return palabra[::-1].upper()
invertir = invertir_palabra('python')
print(invertir)

def chequear_numero(numero):
    return numero in range(0,101) #el nº está entre 0 y 100?
resultado = chequear_numero(323)
print(resultado)

# FUNCIONES DINÁMICAS
# Función que indica si hay algún nº de la lista entre 100 y 1000
def chequear_lista(lista):
    for n in lista:
        if n in range(100,1001):
            return True
        else:
            pass
    return False
resultado = chequear_lista([98,99,102])
print(resultado)

#Función que indica si hay algún nº de la lista entre 100 y 1000
def imprimir_lista(lista):
    lista_numeros = []
    for n in lista:
        if n in range(100,1001):
            lista_numeros.append(n) # con append metemos los nº en la lista_numeros
        else:
            pass
    return lista_numeros
resultado = imprimir_lista([23,12,98,376,102,532])
print(resultado)

# Función que devuelve FALSE si encuentra algún nº negativo y TRUE si todos son positivos
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
lista_numeros = todos_positivos([1,-50,502,-5000,755,600,33,61])
print(lista_numeros)

# Función que suma los números de una lista si están entre 1 y 1000
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(1,1000):
            suma += n
        else:
            pass
    return suma
lista_numeros = suma_menores([2,5,2,8])
print(lista_numeros)

# Función que cuenta la cantidad de numeros pares de una lista
def cantidad_pares(lista):
    cantidad = 0
    for n in lista:
        if n % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad
lista_numeros = cantidad_pares([2,3,4,5,6])
print(lista_numeros)