import numpy as np

class Individual:
    def __init__(self, position):
        self.position = position
        self.fitness = None

def objective_function(x):
    f = []
    for i in range(len(x)-1):
        f.append(100*(x[i]**2-x[i+1])**2 + (x[i]-1)**2)
    return np.sum(f)

def spider_monkey_optimization(objective_function, bounds, max_iterations, num_monkeys, num_dimensions, max_evaluations):
    monkeys = [Individual(np.random.uniform(bounds[:, 0], bounds[:, 1], num_dimensions)) for _ in range(num_monkeys)]
    best_monkey = min(monkeys, key=lambda x: objective_function(x.position))
    evaluations = 0
    all_results = []
    while evaluations < max_evaluations:
        for monkey in monkeys:
            if evaluations >= max_evaluations:
                return all_results
            candidate_monkey = monkey.position + np.random.uniform(-1, 1, num_dimensions) * (monkey.position - best_monkey.position)
            for j in range(num_dimensions):
                if candidate_monkey[j] < bounds[j][0] or candidate_monkey[j] > bounds[j][1]:
                    candidate_monkey[j] = np.random.uniform(bounds[j][0], bounds[j][1])
            candidate_fitness = objective_function(candidate_monkey)
            if candidate_fitness < objective_function(monkey.position):
                monkey.position = candidate_monkey
                monkey.fitness = candidate_fitness
                evaluations += 1
                if candidate_fitness < objective_function(best_monkey.position):
                    best_monkey = monkey
        all_results.append(objective_function(best_monkey.position))
    return all_results

if __name__ == "__main__":
    # Definindo os limites do espaço de busca
    bounds = np.array([[-100, 100]] * 10)  # Espaço de busca: x = [-100, 100] para cada dimensão

    # Definindo os parâmetros do algoritmo
    max_iterations = 51
    num_monkeys = 200  # Tamanho da população
    num_dimensions = 10  # Dimensão do problema
    max_evaluations = 10000 * num_dimensions  # MaxFES: 10000 * D

    # Executando o algoritmo SMO
    results = spider_monkey_optimization(objective_function, bounds, max_iterations, num_monkeys, num_dimensions, max_evaluations)

    # Calculando as métricas
    best_result = min(results)
    mean_result = np.mean(results)
    median_result = np.median(results)
    worst_result = max(results)
    std_deviation = np.std(results)

    # Imprimindo os resultados
    print("Melhor resultado:", best_result)
    print("Média dos resultados:", mean_result)
    print("Mediana dos resultados:", median_result)
    print("Pior resultado:", worst_result)
    print("Desvio padrão dos resultados:", std_deviation)
