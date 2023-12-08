# Proyecto 'Polygon Area calculator' perteneciente al curso 'Scientific Computing with Python' de FCC

# Experimentos para el proyecto 'Probability Calculator'

from proyectos.p21_ProbabilityCalculator_FCC import Hat, experiment

# Experimento para calcular la probabilidad de sacar al menos 1 bola roja y 2 bolas verdes:
hat = Hat("red", "green", "green", "blue", "blue", "blue")
expected_balls = {"red": 1, "green": 2}
num_balls_drawn = 3
num_experiments = 10000

probability = experiment(hat=hat,
                         expected_balls=expected_balls,
                         num_balls_drawn=num_balls_drawn,
                         num_experiments=num_experiments)
print(f"Probabilidad de sacar al menos 1 bola roja y 2 bolas verdes: {probability:.4f}")
