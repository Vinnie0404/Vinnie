import numpy as np
import random

distances = np.array([
    [0, 29, 20, 21, 16, 31],
    [29, 0, 15, 29, 28, 40],
    [20, 15, 0, 15, 14, 25],
    [21, 29, 15, 0, 4, 12],
    [16, 28, 14, 4, 0, 8],
    [31, 40, 25, 12, 8, 0]
])


num_cities = len(distances)
num_ants = 10
num_iterations = 50

alpha = 1          # pheromone importance
beta = 3           # distance importance (increased)
evaporation = 0.6  # higher evaporation → more exploration
Q = 100

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))


# 🔹 Probability function
def probability(from_city, visited):
    probs = []

    for to_city in range(num_cities):
        if to_city not in visited:
            tau = pheromone[from_city][to_city] ** alpha
            eta = (1 / distances[from_city][to_city]) ** beta
            probs.append(tau * eta)
        else:
            probs.append(0)

    total = sum(probs)

    # ✅ Handle zero probability (important fix)
    if total == 0:
        probs = [1/(num_cities - len(visited)) if i not in visited else 0 for i in range(num_cities)]
    else:
        probs = [p / total for p in probs]

    return probs


# 🔹 Construct solution (tour)
def construct_solution():
    start = random.randint(0, num_cities - 1)
    tour = [start]

    while len(tour) < num_cities:
        probs = probability(tour[-1], tour)
        next_city = np.random.choice(range(num_cities), p=probs)
        tour.append(int(next_city))  # convert numpy int → normal int

    tour.append(start)  # return to start
    return tour


# 🔹 Calculate total distance
def tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distances[tour[i]][tour[i+1]]
    return length


best_tour = None
best_length = float('inf')

for iteration in range(num_iterations):

    all_tours = []
    all_lengths = []

    for ant in range(num_ants):
        tour = construct_solution()
        length = tour_length(tour)

        all_tours.append(tour)
        all_lengths.append(length)

        if length < best_length:
            best_length = length
            best_tour = tour

    # 🔹 Evaporation
    pheromone *= (1 - evaporation)

    # 🔹 Update pheromones (normal update)
    for i in range(num_ants):
        for j in range(len(all_tours[i]) - 1):
            a = all_tours[i][j]
            b = all_tours[i][j + 1]
            pheromone[a][b] += Q / all_lengths[i]

    # 🔥 Elitist update (IMPORTANT)
    for i in range(len(best_tour) - 1):
        a = best_tour[i]
        b = best_tour[i + 1]
        pheromone[a][b] += Q / best_length

    print(f"Iteration {iteration}: Best Length = {best_length}")


# 🔹 Final Output
best_tour = [int(x) for x in best_tour]

print("\nBest Tour:", best_tour)
print("Best Distance:", best_length)
