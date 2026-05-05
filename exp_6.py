#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L

import random

# Objective function (example: maximize f(x) = x^2)
def fitness(x):
    return x * x

# Generate initial population
def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

# Clone antibodies
def clone(population, clone_factor=3):
    clones = []
    for ind in population:
        clones.extend([ind] * clone_factor)
    return clones

# Mutation
def mutate(clones, mutation_rate=0.1):
    mutated = []
    for c in clones:
        if random.random() < mutation_rate:
            c += random.uniform(-1, 1)
        mutated.append(c)
    return mutated

# Select best individuals
def select_best(population, size):
    return sorted(population, key=fitness, reverse=True)[:size]

# Main CSA
def clonal_selection():
    pop_size = 6
    generations = 10

    population = initialize_population(pop_size)

    for gen in range(generations):
        print(f"\nGeneration {gen+1}")

        # Evaluate
        population = select_best(population, pop_size)
        print("Best:", population[0], "Fitness:", fitness(population[0]))

        # Clone
        clones = clone(population)

        # Mutate
        mutated = mutate(clones)

        # Select next generation
        population = select_best(mutated, pop_size)

    best_solution = max(population, key=fitness)
    print("\nOptimal Solution:", best_solution)
    print("Max Fitness:", fitness(best_solution))

# Run
clonal_selection()
