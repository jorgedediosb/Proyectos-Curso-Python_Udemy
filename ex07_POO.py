# Ejercicios lección 7 - PROGRAMACIÓN ORIENTADA A OBJETOS (Clases, métodos y atributos)

# CLASES
# Clase llamada Personaje y un objeto a partir de ella, llamado harry_potter
class Personaje:
    pass #indicamos pass ya que la clase no tiene nada más
harry_potter = Personaje()
# Si necesitásemos varias 'instancias u objetos' a partir de la clase principal:
hermione = Personaje()
hagrid = Personaje()
sirius_black = Personaje()

# ATRIBUTOS
# De instancia:
class Pajaro:
    alas = True #Podemos especificar que en la clase 'pájaro', todos tienen 'alas', independientemente del pájaro
    def __init__(self, parametro1, parametro2): # __init__ es el tipo de método
        self.atributo1 = parametro1 #atributo y parámetro pueden tener el mismo nombre (xj 'color')
        self.atributo2 = parametro2
mi_pajaro = Pajaro('rojo', 'Tucán')
print(mi_pajaro.atributo1)
print(mi_pajaro.atributo2)

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
casa_blanca = Casa('blanco', '4')

class Cubo:
    caras = 6 # Como nunestros cubos siempre tendrán 6 caras, se incluye así
    def __init__(self,color):
        self.color = color
cubo_rojo = Cubo('rojo')

class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje('Humano',True,'17')

# MÉTODOS
# De instancia:

# Clase Perro que debe poder ladrar.
class Perro:
    def ladrar(self):
        print('Guau!')
mi_perro = Perro()
mi_perro.ladrar()

# Mago que salce un hechizo
class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')
merlin = Mago()
merlin.lanzar_hechizo()

# Alarma que se posponga 15 minuntos
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
mi_alarma = Alarma()
mi_alarma.postergar(15)

# método de instancia que reste en -1 la cantidad de flechas que tiene una instancia de Personaje,
# que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
personaje = Personaje(10)
print(personaje.cantidad_flechas)
personaje.lanzar_flecha()
print(personaje.cantidad_flechas)

# Métodos estáticos:
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
Mascota.respirar()

# Métodos de clases
class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("El jugador ha sido revivido")
print(Jugador.vivo)
Jugador.revivir()
print(Jugador.vivo)