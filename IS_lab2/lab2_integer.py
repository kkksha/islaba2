# Импортирование генетического алгоритма
from pyeasyga.pyeasyga import GeneticAlgorithm 
import random
import numpy as np

# Представление данных
# Данные - множество нулей с одной единицей на какой-либо позиции
# Позиция отражает положение x на оси абсцисс от -2 до 2
seed_data = [0] * 200
seed_data.append(1)

# Иницилизируем генетический алгоритм
#(начальные данные, кол-во особей в популяции, кол-во генераций, вероятность применения оператора скрещивания, вероятность применения мутации к гену, вкл. выбор лучшей особи, максимизация целевой функции)
ga = GeneticAlgorithm(seed_data, 400, 200, 0.7, 0.05, True, False)

# Отдельная особь, как случайное положение х
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual
    
ga.create_individual = create_individual

# Одноточечный кроссинговер
def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b
    return child_1, child_2

ga.crossover_function = crossover

# Целочисленная мутация
def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]

ga.mutate_function = mutate

# Рулеточная селекция
def selection(population):
    return random.choice(population)

ga.selection_function = selection

# Функция приспособленности
# Ищет такой х, при котором значение функции минимально
def fitness (individual, data):
    fitness = float("inf")
    x = -2
    for item in individual:
        if item != 1:
            x += 0.01
        else:
            fitness = x**2 + 4 
            break 
    return fitness

ga.fitness_function = fitness
ga.run()
# Вывод самой приспособленной особи
print(ga.best_individual()) 