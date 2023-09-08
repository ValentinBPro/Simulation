import random
import Simulation

# Fonction de fitness (objectif à maximiser : le solde final)
def fitness(stop_loss, take_profit):
    actions = [3,4,5,4,3,2,1,2,3,2,1,2,3,4,3]
    final_balance = Simulation.simulate_trading(actions, stop_loss, take_profit)
    return final_balance

# Fonction de création de la population initiale
def create_population(population_size):
    population = []
    for _ in range(population_size):
        stop_loss = random.uniform(0.01, 0.2)  # Valeurs aléatoires pour StopLoss entre 1% et 20%
        take_profit = random.uniform(0.05, 0.3)  # Valeurs aléatoires pour TakeProfit entre 5% et 30%
        population.append((stop_loss, take_profit))
    return population

# Algorithme génétique
def genetic_algorithm(population_size, generations):
    population = create_population(population_size)
    
    for generation in range(generations):
        # Évaluez la fitness de chaque individu dans la population
        fitness_scores = [fitness(stop_loss, take_profit) for stop_loss, take_profit in population]
        
        # Sélectionnez les individus les mieux adaptés pour la reproduction
        selected_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)
        selected_population = [population[i] for i in selected_indices[:population_size // 2]]
        
        # Créez de nouveaux individus par croisement (crossover)
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(selected_population, k=2)
            crossover_point = random.randint(1, len(parent1) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            new_population.append(child)
        
        # Remplacez l'ancienne population par la nouvelle
        population = new_population
        
    # Sélectionnez le meilleur individu de la dernière génération
    best_individual = max(population, key=lambda ind: fitness(ind[0], ind[1]))
    return best_individual

# Exécution de l'algorithme génétique
best_stop_loss, best_take_profit = genetic_algorithm(population_size=50, generations=100)
best_balance = fitness(best_stop_loss, best_take_profit)

print(f"Meilleur StopLoss: {best_stop_loss:.4f}")
print(f"Meilleur TakeProfit: {best_take_profit:.4f}")
print(f"Solde final avec les meilleurs paramètres: {best_balance:.2f}")
