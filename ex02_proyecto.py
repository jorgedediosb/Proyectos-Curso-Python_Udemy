nombre = input("Nombre de empleado:")
ventas = int(input("¿Cuantas ventas has hecho hoy?")) #al guardarse como string lo transformo a int
comisiones = round((ventas * 13)/ 100, 2) #comisión del 13%
print(f"{nombre} hoy recibes {comisiones} euros por tus ventas.")