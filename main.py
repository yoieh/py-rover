from pyrover import CLItxt
from pyrover import Grid
from pyrover import Rover

MAX_GRID_SIZE = 100


class Main():
    def __init__(self):
        self.cli = CLItxt(MAX_GRID_SIZE)
        self.grid = Grid(self.cli.grid_size[0], self.cli.grid_size[1], 1)
        self.simulated_rover = Rover(
            self.grid, self.cli.start_pos[0], self.cli.start_pos[1], self.cli.start_pos[2])
        self.rover = Rover(
            self.grid, self.cli.start_pos[0], self.cli.start_pos[1], self.cli.start_pos[2])

    def run(self):
        print(self.cli.grid_size)
        print(self.cli.start_pos)
        print(self.cli.commands)

        self.simulated_rover.take_input(self.cli.commands)
        self.simulated_rover.run()
        calculated_end_position = self.simulated_rover.get_last_position()

        print()
        print("Show start position R and end position X")
        self.print_as_grid(self.rover, calculated_end_position)
        self.rover.take_input(self.cli.commands)
        self.rover.run()
        end_position = self.rover.get_last_position()

        print()
        print("Show where the rover ended up")
        self.print_as_grid(self.rover, end_position)

    def print_as_grid(self, rover: Rover, end_pos):
        for i in range(self.grid.height):
            for j in range(self.grid.width):
                if rover.x == j and rover.y == i:
                    print("R", end=" ")
                elif end_pos[0] == j and end_pos[1] == i:
                    print("X", end=" ")
                else:
                    print(self.grid.get_cell(i, j), end=" ")
            print()


if __name__ == "__main__":
    main = Main()
    main.run()
