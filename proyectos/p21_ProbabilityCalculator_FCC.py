# Proyecto 'Polygon Area calculator' perteneciente al curso 'Scientific Computing with Python' de FCC

import random

class Hat:
    '''
    La clase Hat tiene un constructor __init__ que toma un número variable de argumentos
    para especificar la cantidad de bolas de cada color en el sombrero.
    Las bolas se almacenan en la lista contents, donde cada elemento es una cadena
    que representa un color.
    El método draw elimina las bolas del sombrero y las devuelve en una lista.
    '''
    def __init__(self, *balls):
        self.contents = list(balls)

    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Realiza una serie de experimentos utilizando el sombrero y los parámetros especificados.
    Se copia el sombrero original para mantenerlo intacto durante los experimentos.
    Luego, se realiza un experimento dibujando 'num_balls_drawn'
    y se verifica si contiene las bolas esperadas.
    Se lleva un contador de experimentos exitosos y se devuelve la probabilidad estimada.
    '''
    count_successful = 0

    for _ in range(num_experiments):
        hat_copy = Hat(*hat.contents)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        success = True
        for color, quantity in expected_balls.items():
            if drawn_balls.count(color) < quantity:
                success = False
                break

        if success:
            count_successful += 1

    return count_successful / num_experiments

'''
# Experimento para calcular la probabilidad de sacar al menos 1 bola roja y 2 bolas verdes:
# Este experimento está también en el archivo 'p20_ProbabilityCalculator_Experiments_FCC.py'

hat = Hat("red", "green", "green", "blue", "blue", "blue")
expected_balls = {"red": 1, "green": 2}
num_balls_drawn = 3
num_experiments = 10000

probability = experiment(hat=hat,
                         expected_balls=expected_balls,
                         num_balls_drawn=num_balls_drawn,
                         num_experiments=num_experiments)
print(f"Probabilidad de sacar al menos 1 bola roja y 2 bolas verdes: {probability:.4f}")
'''