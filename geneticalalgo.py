import random
import time

# --- GA Configuration Parameters ---
TARGET_SUM = 100            # The ideal fitness score
SEQUENCE_LENGTH = 10        # Number of 'genes' in a chromosome
GENE_RANGE = (0, 10)        # Possible values for each gene
POPULATION_SIZE = 50        # Number of solutions in each generation
MUTATION_RATE = 0.05        # Probability of a gene mutating (5%)
MAX_GENERATIONS = 500       # Maximum number of iterations

# Individual representation: A list of integers (the "chromosome")
# Fitness: The sum of the integers in the list

def create_individual():
    """Generates a single random chromosome (initial solution)."""
    return [random.randint(GENE_RANGE[0], GENE_RANGE[1]) for _ in range(SEQUENCE_LENGTH)]

def fitness_function(individual):
    """Calculates the fitness score (sum of elements). Higher is better."""
    return sum(individual)

def selection(population):
    """
    Selects the best two parents using Tournament Selection.
    Picks three random individuals and chooses the two fittest among them.
    """
    K = 3 # Tournament size
    
    # Tournament 1
    tournament_pool_1 = random.sample(population, K)
    parent1 = max(tournament_pool_1, key=fitness_function)

    # Tournament 2 (Ensures parent2 is not the same instance as parent1)
    tournament_pool_2 = random.sample(population, K)
    parent2 = max(tournament_pool_2, key=fitness_function)
    
    return parent1, parent2

def crossover(parent1, parent2):
    """
    Performs Single-Point Crossover to generate one child.
    """
    # Choose a random point to split the genes
    crossover_point = random.randint(1, SEQUENCE_LENGTH - 1)
    
    # Create the child by combining parts of the two parents
    child_genes = parent1[:crossover_point] + parent2[crossover_point:]
    
    return child_genes

def mutation(individual):
    """
    Applies mutation to the individual based on the MUTATION_RATE.
    A mutated gene is replaced by a new random value within the allowed range.
    """
    for i in range(SEQUENCE_LENGTH):
        if random.random() < MUTATION_RATE:
            # Mutate the gene at index i
            individual[i] = random.randint(GENE_RANGE[0], GENE_RANGE[1])
    return individual

def genetic_algorithm_solve():
    """
    The main loop for the Genetic Algorithm.
    """
    # 1. INITIALIZATION
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    generation = 0
    
    print("--- Starting Genetic Algorithm (Target Sum: 100) ---")

    while generation < MAX_GENERATIONS:
        # Evaluate current population and find the best solution
        current_best = max(population, key=fitness_function)
        best_fitness = fitness_function(current_best)

        print(f"Gen {generation:03d} | Best Fitness: {best_fitness:03d} | Best Solution: {current_best}")

        # Stopping condition: If we found the optimal solution
        if best_fitness >= TARGET_SUM:
            print(f"\nSUCCESS! Target fitness reached in generation {generation}.")
            break

        # 2. SELECTION and 3. REPRODUCTION
        new_population = []
        # Keep the top two best individuals (Elitism) for guaranteed propagation
        new_population.extend(sorted(population, key=fitness_function, reverse=True)[:2])

        # Fill the rest of the new population
        for _ in range(POPULATION_SIZE - len(new_population)):
            # Select parents
            parent1, parent2 = selection(population)
            
            # Crossover to create a child
            child = crossover(parent1, parent2)
            
            # 4. MUTATION
            mutated_child = mutation(child)
            
            new_population.append(mutated_child)

        # Update population and generation count
        population = new_population
        generation += 1
        
    final_best = max(population, key=fitness_function)
    print("\n--- Final Results ---")
    print(f"Generations run: {generation}")
    print(f"Optimal Solution Found: {final_best}")
    print(f"Final Fitness Score: {fitness_function(final_best)}")


if __name__ == "__main__":
    # Ensure reproducibility for testing (optional)
    random.seed(int(time.time()))
    
    genetic_algorithm_solve()
