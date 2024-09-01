# Programa que ejecuta el algoritmo Luhn para verificar la validez de un número de tarjeta de crédito

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # El número de tarjeta se invierte para procesar los dígitos de derecha a izquierda.
    card_number_reversed = card_number[::-1]
    # Se seleccionan todos los dígitos en posiciones impares
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        # Los dígitos se convierten a enteros y se suman.
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Se seleccionan todos los dígitos en posiciones pares.
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        # Cada uno de estos dígitos se multiplica por 2.
        number = int(digit) * 2
        # Si el resultado de la multiplicación es mayor o igual a 10, se suman los dígitos de este número 
        # Si el resultado es 14, se suman 1 + 4 para obtener 5.
        if number >= 10:
            number = (number // 10) + (number % 10)
        # Se suman los valores procesados.
        sum_of_even_digits += number
    # Se verifica si la suma de los impares y los pares es divisible por 10.
    # Si lo es, el número de tarjeta es válido según el algoritmo Luhn.
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    # Crear una tabla de traducción que elimina los guiones (-) y espacios ( ) del número de tarjeta.
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Número de tarjeta limpio, sin guiones ni espacios, listo para ser procesado.
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()