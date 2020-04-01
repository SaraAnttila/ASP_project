class Cell():
    def __init__(self, isAlive, x, y):
        """
        Class holding the status (alive) and position of the cell in the grid.
        """
        self.isAlive = isAlive
        self.x = x
        self.y = y

    def __str__(self):
        return  str(1) if self.isAlive else str(0)

    def __repr__(self):
        return self.__str__()
