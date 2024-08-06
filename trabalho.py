import numpy as np

# Função objetivo de exemplo (minimizar a função quadrática f(x) = x^2)
def objective_function(x):
    f = []
    for i in range(len(x) - 1):
        f.append(100 * (x[i] ** 2 - x[i + 1]) ** 2 + (x[i] - 1) ** 2)
    return np.sum(f)

# Classe de Aranha
class Spider:
    def __init__(self, position):
        self.position = position  # Posição da aranha no espaço de busca
        self.fitness = objective_function(position)  # Avaliação da aptidão da aranha

# Função para criar uma população inicial de aranhas
def create_population(population_size, dimension):
    population = []
    for i in range(population_size):
        position = np.random.rand(dimension) * 10  # Gerar posição aleatória no intervalo [0, 10]
        population.append(Spider(position))
    return population

# Algoritmo de otimização Spider Monkey
def spider_monkey_optimization(population_size, dimension, max_iterations):
    population = create_population(population_size, dimension)
    best_spider = min(population, key=lambda spider: spider.fitness)  # Inicializar a melhor aranha na população
    for _ in range(max_iterations):
        # Atualizar a posição de cada aranha na população
        for spider in population:
            new_position = spider.position + (np.random.random(size=dimension) - 0.5)  # Movimento aleatório
            new_position = np.clip(new_position, 0, 10)  # Limitar a posição ao intervalo [0, 10]
            spider.position = new_position
            spider.fitness = objective_function(new_position)  # Atualizar a avaliação de aptidão da aranha
            if spider.fitness < best_spider.fitness:
                best_spider = spider  # Atualizar a melhor aranha se necessário
    return best_spider

# Parâmetros do algoritmo
population_size = 50
dimension = 2
max_iterations = 1000

# Executar o algoritmo e obter a melhor solução
best_spider = spider_monkey_optimization(population_size, dimension, max_iterations)

# Exibir a melhor solução encontrada
print("Melhor posição encontrada:", best_spider.position)
print("Melhor valor de aptidão encontrado:", best_spider.fitness)
