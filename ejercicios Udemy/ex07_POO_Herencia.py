# Ejercicios lección 7 - PROGRAMACIÓN ORIENTADA A OBJETOS
# HERENCIA

# Las clases 'Alumno', 'Mascota' y 'Automovil' heredan los atributos de 'Persona', 'Mascota' y 'Vehiculo'
class Persona:
    def __init__(self, nombre, edad): #Atributos de instancia
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas): #Atributos de instancia
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
class Perro(Mascota):
    pass

class Vehiculo:
    def acelerar(self): #Método de clase
        pass
    def frenar(self): #Método de clase
        pass
class Automovil(Vehiculo):
    pass

# Herencia Múltiple
# 'Hija' hereda de 'Madre' su forma de trabajar (no de 'Padre') y de 'Padre' el atributo 'reir'
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre): #herencia múltiple
    pass


# 'Ornintorrinco' hereda los atributos:
# poner_huevos(), tiene_pico, vertebrado, venenoso, nadar(), caminar(), amamantar()
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass

# Herencia modificada y nueva:
# el 'hijo' hereda del 'padre' todos los atributos pero modifica su hobby y ademas habla inglés
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
    def idioma_ingles(self):
        return "Hablo inglés"