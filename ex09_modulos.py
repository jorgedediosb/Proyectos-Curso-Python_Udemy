# Ejercicios lección 9 - MÓDULOS PYTHON

# MÓDULO COLLECTIONS
from collections import Counter
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print(contador)

from collections import defaultdict
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44
print(mi_diccionario)

from collections import deque
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)

from collections import namedtuple
mi_tupla = namedtuple('Persona', ['nombre', 'edad', 'altura'])
persona1 = Persona('Marcos', 39, 1.78)
print(persona1)


# MÓDULO DATETIME
from datetime import date
mi_fecha = date(1999, 2, 3)

from datetime import date
hoy = date.today()

from datetime import datetime
minutos = datetime.now().minute