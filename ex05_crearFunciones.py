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
    return numero in range(0,101)
resultado = chequear_numero(323)
print(resultado)