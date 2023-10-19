# Ejercicios lección 5 - Problemas prácticos resumen lección

# Problema 1
# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1,num2,num3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort() #lista ordenada
        return (lista)[1] #[1] es el nº intermedios de los 3 (posición 2) 

print(devolver_distintos(1,2,4))


# Problema 2
# Función que reciba cualquier palabra como parámetro,
# y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
# Al invocar la función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def letras_unicas(palabra):
    letras = list(set(palabra)) #set da elementos únicos e irrepetibles
    letras.sort()
    return letras

print(letras_unicas('pajaro'))


# Problema 3
# Función que requiera una cantidad indefinida de argumentos.
# Que devuelva True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
# Por ejemplo: (5,6,1,0,0,9,3,5) >>> True // (6,0,5,1,0,3,0,1) >>> False

def dos_ceros(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False
    
print(dos_ceros(5, 6, 1, 3, 0, 9, 3, 5))


# Problema 4
# Función con un argumento que  muestre todos los números primos existentes en el rango que va desde cero hasta ese número incluido,
# y va a devolver la cantidad de números primos que encontró.
# Por convención el 0 y el 1 no se consideran primos.

def contar_primos(num):
    primos = []
    for num in range(2, num + 1): #nºs a partir de 2
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1): #verificar si "num" es divisible por algún número entre 2 y su raíz cuadrada para evitar que lo calcule según el resto de nºs.
            if num % i == 0: # si "num" es divisible por "i" no es primo.
                es_primo = False
                break
        if es_primo:
            primos.append(num) #si es primo se agrega a la lista
            print(num)
    cantidad_primos = len(primos)
    return cantidad_primos

cantidad = contar_primos(20)
print("Cantidad nºs primos encontrados:", cantidad)