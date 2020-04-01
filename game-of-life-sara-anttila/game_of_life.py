import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grid import Grid
from grid import generate_seed

"""
Game runner
"""
class Game():
    def __init__(self, grid):
        self.grid = grid
        self.state = self.render_able()

    def update(self, data):
        self.grid.update(N)
        self.state = self.render_able()
        mat.set_data(self.state)
        return [mat]

    def render_able(self):
        new_state = []
        state = self.grid.state
        for i in range(N):
            grid_row = []
            row = state[i]
            for j in range(N):
                alive = 255 if row[j].isAlive == 1 else 0
                grid_row.append(alive)
            new_state.append(grid_row)
        return new_state

    def __str__(self):
        return str(self.grid)

"""
Decide the size of the grid
"""
print('Enter the size of the square grid')
N = int(input())

print('Enter type of seed. 1 = random seed, 2 = glider seed, 3 = line seed, 4 = cross seed')
chosen_seed = input()

"""
Run the game
"""
game = Game(generate_seed(N, chosen_seed))
"""
Animation
"""
fig, ax = plt.subplots()
mat = ax.matshow(game.state)
ani = animation.FuncAnimation(fig, game.update, interval=50,
                              save_count=50)
plt.show()
