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

    def print_as_grid(self, rover):
        for i in range(self.height):
            for j in range(self.width):
                if rover.x == j and rover.y == i:
                    print("R", end=" ")
                elif rover.calculated_end_position[0] == j and rover.calculated_end_position[1] == i:
                    print("X", end=" ")
                else:
                    print(self.grid[i * self.width + j], end=" ")
            print()
