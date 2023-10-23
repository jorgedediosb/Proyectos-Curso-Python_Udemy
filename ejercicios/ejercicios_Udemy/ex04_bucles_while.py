#Ejercicios lección 4 - Bucles / loops - WHILE

monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas!")
    monedas -= 1 #evitamos bucle infinito restando 1 a cada iteración hasta igualar a 0.
                 #es lo mismo que: monedas = monedas - 1
else:
    print("No tengo más dinero")

#Los bucles while suelen depender del comportameniendo del usuario
respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Quieres continuar? (s/n): ")
else:
    print("FIN")

#Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

#Loop que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
#Si el número es divisible por 5, mostrar dicho número en pantalla
#Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
