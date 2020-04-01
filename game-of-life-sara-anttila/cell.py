class Cell():
    def __init__(self, isAlive, x, y):
        """
        Class holding the status (alive) and position of the cell in the grid.
        """
        self.isAlive = isAlive
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.isAlive) + " (" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()
