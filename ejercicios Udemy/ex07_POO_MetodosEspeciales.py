# Ejercicios lección 7 - PROGRAMACIÓN ORIENTADA A OBJETOS - MÉTODOS ESPECIALES

# Los métodos especiales se indican con __nombre__:

# __init__ y __str__:
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self): # __str__ permite imprimir un objeto
        return f'"{self.titulo}", de {self.autor}'
    

# __len__ permite mostrar la longitud del método del objeto:
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
    
# __del_ permite eliminar un objeto:
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")