import random
from deap import base, creator, tools, algorithms
from multiprocessing import Pool, freeze_support

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval_func(individual):
    return (individual[0]**2,)

toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    pool = Pool()   # ✅ ONLY HERE
    toolbox.register("map", pool.map)

    population = toolbox.population(n=30)

    for gen in range(10):
        offspring = algorithms.varAnd(population, toolbox, 0.5, 0.2)

        fits = toolbox.map(toolbox.evaluate, offspring)

        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit

        population = toolbox.select(offspring, k=len(population))
        best = max(population, key=lambda x: x.fitness.values)
        print(f"Generation {gen}: Best Individual = {best}, Fitness = {best.fitness.values}")

    pool.close()
    pool.join()


if __name__ == "__main__":
    freeze_support()   # ✅ IMPORTANT for Windows
    main()
