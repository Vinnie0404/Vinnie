import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=500, n_features=10, 
                           n_classes=3, n_informative=5,
                           random_state=42)

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

POP_SIZE = 50
CLONE_FACTOR = 5
MUTATION_RATE = 0.1
GENERATIONS = 5

def initialize_population():
    return np.random.rand(POP_SIZE, X_train.shape[1])

def affinity(antibody, antigen):
    return 1 / (1 + np.linalg.norm(antibody - antigen))

def classify(antibody, X_train, y_train):
    affinities = [affinity(antibody, x) for x in X_train]
    idx = np.argmax(affinities)
    return y_train[idx]

def evaluate_population(population):
    scores = []
    for antibody in population:
        preds = [classify(antibody, X_train, y_train) for _ in X_train]
        score = accuracy_score(y_train, preds)
        scores.append(score)
    return np.array(scores)

def clone_and_mutate(population, scores):
    new_population = []
    
    sorted_idx = np.argsort(scores)[::-1]
    selected = population[sorted_idx[:POP_SIZE // 2]]
    
    for antibody in selected:
        clones = [antibody.copy() for _ in range(CLONE_FACTOR)]
        
        for clone in clones:
            mutation = MUTATION_RATE * np.random.randn(*clone.shape)
            clone += mutation
            clone = np.clip(clone, 0, 1)
            new_population.append(clone)
    
    return np.array(new_population[:POP_SIZE])

population = initialize_population()

for gen in range(GENERATIONS):
    scores = evaluate_population(population)
    population = clone_and_mutate(population, scores)
    print(f"Generation {gen+1}, Best Score: {np.max(scores):.4f}")

scores = evaluate_population(population)
best_idx = np.argmax(scores)
memory_cell = population[best_idx]

def predict(X_test):
    preds = []
    for x in X_test:
        preds.append(classify(memory_cell, X_train, y_train))
    return np.array(preds)

y_pred = predict(X_test)

print("\nTest Accuracy:", accuracy_score(y_test, y_pred))