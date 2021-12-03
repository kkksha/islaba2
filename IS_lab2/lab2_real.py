from pyeasyga.pyeasyga import GeneticAlgorithm
import random
import numpy as np

# Формат задания значений (y(x), [x])
data = (4.0, [-2.0])

# Параметры работы генетического алгоритма
# (начальные данные, кол-во особей в популяции, кол-во генераций, вероятность применения оператора скрещивания, вероятность применения мутации к гену, вкл. выбор лучшей особи, максимизация целевой функции)
ga = GeneticAlgorithm(data, 20, 30, 0.7, 0.01, True, False)

# Функция создания начальной популяции
def create_individual(data):
    # Вещественное кодирование
    ind = [random.uniform(-4.0, 4.0)]
    # Вывод начальной популяции на экран
    print(ind[0] * ind[0] + 4, ind)
    return ind #[random.uniform(-4.0, 4.0) for _ in range(len(data))]
    
ga.create_individual = create_individual

# Функция кроссинговера ГА (арифметический кроссинговер, lambda = 0.2)
def crossover(parent_1, parent_2): 
    child_1 = [parent_1[0] * 0.2 + parent_2[0] * 0.8]
    child_2 = [parent_2[0] * 0.2 + parent_1[0]* 0.8]
    return child_1, child_2

ga.crossover_function = crossover

# Функция мутации для вещественного кодирования
def mutate(individual): 
    rnd = np.random.normal(0, 0.5)
    if rnd < -0.5:
        rnd = -0.5
    elif rnd > 0.5:
        rnd = 0.5
    individual[0] = individual[0] + rnd

ga.mutate_function = mutate

# Функция селекции / турнирный отбор
def selection(population): 
    ind1 = random.choice(population)
    ind2 = random.choice(population)
    if ind1.fitness < ind2.fitness:
        return ind1
    else:
        return ind2

ga.selection_function = selection

def fitness (individual, data): #Целевая функция
    return individual[0] * individual[0] + 4 #Значение целевой функции 
    
ga.fitness_function = fitness
ga.run()
# Вывод лучшей особи популяции (Наше решение)
print("\nBest individual: ", ga.best_individual(), "\n")

# Вывод всех особей популяции в последнем поколении
for individual in ga.last_generation(): 
  print(individual)