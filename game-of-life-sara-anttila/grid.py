from cell import Cell
import numpy as np
"""
Generating and updating the grid
"""
class Grid():
    def __init__(self, seed, N):
        """
        init holds the seed and the grid generation
        """
        self.seed = seed
        self.state = self.generate_grid(seed, N)
    def generate_grid(self, seed, N):
        grid = []
        for i in range(N):
            grid_row = []
            row = seed[i]
            for j in range(N):
                alive = row[j] == 1
                grid_row.append(Cell(alive, i, j))
            grid.append(grid_row)
        return grid
    def update(self, N):
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

"""
Setting up the initial pattern, the seed of the system.
"""
def generate_seed(N, chosen_seed):
    if chosen_seed == '1':
        """
        #1 Random seed
        # """
        p = 0.2 # probability of seed cell starting as alive
        state = [1, 0] # alive or dead
        seed = np.random.choice(state, N**2, [p, 1-p]).reshape(N, N)
        random_grid = Grid(seed, N)
        return random_grid
    elif chosen_seed == '2':
        """
        #2 Glider seed
        """
        glider = [[1, 0, 0],
                  [0, 1, 1],
                  [1, 1, 0]]
        X = np.zeros((N,N))
        X[:3, :3] = glider
        glider_grid = Grid(X, N)
        return glider_grid
    elif chosen_seed == '3':
        """
        #3 Line seed
        """
        X = np.zeros((N,N))
        c = int(N/2)
        X[c,:]= 1
        line_grid = Grid(X, N)
        return line_grid
    elif chosen_seed == '4':
        """
        #4 Cross seed
        """
        X = np.zeros((N,N))
        c = int(N/2)
        X[c,:]= 1
        X[:,c]= 1
        cross_grid = Grid(X, N)
        return cross_grid
    else:
        print('Sorry, unvalid entry')
