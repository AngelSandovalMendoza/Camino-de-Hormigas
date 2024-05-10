import random
import numpy as np
import matplotlib.pyplot as plt

class Ant:
    def __init__(self, x, y, grid_size):
        self.x = x
        self.y = y
        self.grid_size = grid_size

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(self.x, self.grid_size-1))
        self.y = max(0, min(self.y, self.grid_size-1))

class Environment:
    def __init__(self, grid_size, num_food_sources):
        self.grid_size = grid_size
        self.food_sources = [(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(num_food_sources)]
        self.pheromones = np.zeros((grid_size, grid_size))

    def evaporate_pheromones(self, evaporation_rate):
        self.pheromones *= (1 - evaporation_rate)

    def deposit_pheromones(self, x, y, amount):
        self.pheromones[x][y] += amount

    def get_pheromone_intensity(self, x, y):
        return self.pheromones[x][y]

def main():
    grid_size = 20
    num_food_sources = 3
    evaporation_rate = 0.1
    num_iterations = 100
    num_ants = 10

    environment = Environment(grid_size, num_food_sources)
    ants = [Ant(grid_size // 2, grid_size // 2, grid_size) for _ in range(num_ants)]

    fig, ax = plt.subplots()

    for _ in range(num_iterations):
        ax.clear()
        ax.set_title('Ants Simulation')
        ax.set_xlim(0, grid_size-1)
        ax.set_ylim(0, grid_size-1)
        
        for food_source in environment.food_sources:
            ax.scatter(food_source[0], food_source[1], color='green', marker='o', label='Food')

        for ant in ants:
            ant.move()
            ax.scatter(ant.x, ant.y, color='black', marker='o')

            for food_source in environment.food_sources:
                if (ant.x, ant.y) == food_source:
                    environment.deposit_pheromones(ant.x, ant.y, 1)
        
        environment.evaporate_pheromones(evaporation_rate)

        plt.pause(0.1)

    plt.show()

if __name__ == "__main__":
    main()
