import random


class Grid:
    def __init__(self, width, height, obstacles=0):
        self.width = width
        self.height = height
        self.grid = []

        self.create_grid()
        self.generate_obstacles(obstacles)

    # creates 1d array of 0s
    def create_grid(self):
        for i in range(self.height * self.width):
            self.grid.append(0)

    # set random positions to 1
    def generate_obstacles(self, obstacles):
        for i in range(obstacles):
            self.grid[random.randint(0, self.width * self.height - 1)] = 1

    def get_cell(self, x, y):
        return self.grid[y * self.width + x]
