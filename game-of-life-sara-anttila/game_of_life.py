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
    """
    Animation block
    """
    def update(self, data):
        self.grid.update(N)
        self.state = self.render_able()
        mat.set_data(self.state)
        return [mat]
    """
    Iteration block
    """
    def run_game(self, max_iter):
        previous_state = None
        i = 0
        while (self.grid.state != previous_state and i < max_iter):
            i += 1
            previous_state = self.grid.state.copy()
            self.grid.update(N)
        return self.grid

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

# """
# Decide the size of the grid
# """
# print('Enter the size of the square grid')
# N = int(input())
#
# print('Enter type of seed. 1 = random seed, 2 = glider seed, 3 = line seed, 4 = cross seed')
# chosen_seed = input()
# 
# """
# Run the game
# """
# print('Animation or 1000 iterations? [a/i]')
# show = input()
# if show == 'a':
#     """
#     Animation
#     """
#     game = Game(generate_seed(N, chosen_seed))
#     fig, ax = plt.subplots()
#     mat = ax.matshow(game.state)
#     ani = animation.FuncAnimation(fig, game.update, interval=50,
#                                   save_count=50)
#     plt.show()
# elif show =='i':
#     game = Game(generate_seed(N, chosen_seed))
#     max_iter = 1000
#     print(game.run_game(max_iter))
# else:
#     print('Sorry, invalid entry.')
