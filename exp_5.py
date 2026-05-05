#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L

import numpy as np
import random

def nn_error(params):

    return sum([p**2 for p in params]) 

population_size = 20
num_generations = 50
mutation_rate = 0.1

population = [np.random.rand(3) for _ in range(population_size)]

for gen in range(num_generations):

    fitness = [nn_error(ind) for ind in population]

    sorted_pop = [x for _, x in sorted(zip(fitness, population), key=lambda pair: pair[0])]

    new_population = sorted_pop[:2]

    while len(new_population) < population_size:
        p1, p2 = random.sample(sorted_pop[:4], 2)
        child = (p1 + p2) / 2

        if random.random() < mutation_rate:
            child += np.random.normal(0, 0.1, size=3)

        new_population.append(child)

    population = new_population

    print(f"Generation {gen+1}, Best Error: {min(fitness)}")

best_solution = min(population, key=nn_error)
print("\nOptimized Parameters:", best_solution)
