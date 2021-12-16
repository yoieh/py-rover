from pyrover import CLItxt
from pyrover import Grid
from pyrover import Rover

MAX_GRID_SIZE = 100


class Main():
    def __init__(self):
        self.cli = CLItxt(MAX_GRID_SIZE)
        self.grid = Grid(self.cli.grid_size[0], self.cli.grid_size[1], 1)
        self.rover = Rover(
            self.grid, self.cli.start_pos[0], self.cli.start_pos[1], self.cli.start_pos[2])

    def run(self):
        print(self.cli.grid_size)
        print(self.cli.start_pos)
        print(self.cli.commands)

        self.rover.simulate_run_rover(self.cli.commands)

        print()
        print("Show start position R and end position X")
        self.grid.print_as_grid(self.rover)

        self.rover.run_rover()

        print()
        print("Show where the rover ended up")
        self.grid.print_as_grid(self.rover)


if __name__ == "__main__":
    main = Main()
    main.run()
