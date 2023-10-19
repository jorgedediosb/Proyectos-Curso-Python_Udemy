# Ejercicios lección 7 - PROGRAMACIÓN ORIENTADA A OBJETOS - POLIMORFISMO

# Iterador a partir de varios objetos: palabra, lista, tupla
# que muestra la longitud con la función len().
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))


# Iterador a partir de una única lista:
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
gandalf = Mago()
robin = Arquero()
itoku = Samurai()

personajes = [gandalf, robin, itoku]

for personaje in personajes:
    personaje.atacar()


# Función que recibe un objeto
# y ejecuta su método independientemente del tipo de personaje:
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

gandalf = Mago()
robin = Arquero()
itoku = Samurai()

personaje = [gandalf, robin, itoku]

def personaje_defender(personaje):
    personaje.defender()