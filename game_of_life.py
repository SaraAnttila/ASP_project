import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Cell():
    def __init__(self, isAlive, x, y):
        self.isAlive = isAlive
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.isAlive) + " (" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return self.__str__()

class Grid():
    def __init__(self, seed):
        self.seed = seed
        self.state = self.generate_grid(seed)
    def generate_grid(self, seed):
        grid = []
        for i in range(N):
            grid_row = []
            row = seed[i]
            for j in range(N):
                alive = row[j] == 1
                grid_row.append(Cell(alive, i, j))
            grid.append(grid_row)
        return grid
    def update(self):
        old_grid = self.state.copy()
        new_grid = []

        search_min = -1
        search_max = 2

        for i in range(N):
            new_row = []
            new_grid.append(new_row)
            for j in range(N):
                current_cell = old_grid[i][j]
                nr_of_living_cells = 0
                for x in range(search_min, search_max):
                    for y in range(search_min, search_max):
                        if i+x < 0 or i+x > N-1 or j+y <0 or j+y > N-1:
                            continue
                        current_neighbour = old_grid[i+x][j+y]
                        if current_neighbour.isAlive and not (x == 0 and y == 0):
                            nr_of_living_cells += 1

                new_cell = Cell(current_cell.isAlive, i,j)
                if nr_of_living_cells < 2:
                    new_cell.isAlive = False
                if nr_of_living_cells > 3:
                    new_cell.isAlive = False
                if nr_of_living_cells == 3:
                    new_cell.isAlive = True
                new_grid[i].append(new_cell)
        self.state = new_grid
        #print(old_grid)

    def __str__(self):
        return str(self.state)

class Game():
    def __init__(self, grid):
        self.grid = grid
        self.state = self.render_able()
    def update(self, data):

        self.grid.update()

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

# Setting up the initial pattern, the seed of the system.
# """
# """
# #1 Random seed
# """
N =100 # NxN size grid
p = 0.2 # probability of seed cell starting as alive
state = [1, 0] # alive or dead
seed = np.random.choice(state, N**2, [p, 1-p]).reshape(N, N)
#print(seed)


glider = [[1, 0, 0],
          [0, 1, 1],
          [1, 1, 0]]
X = np.zeros((N,N))
X[:3, :3] = glider


randomGrid = Grid(seed)

game = Game(randomGrid)

t = time.time()

fig, ax = plt.subplots()
mat = ax.matshow(game.state)
ani = animation.FuncAnimation(fig, game.update, interval=50,
                              save_count=50)
plt.show()

print(time.time()-t)
