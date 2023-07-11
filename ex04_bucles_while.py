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

numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

