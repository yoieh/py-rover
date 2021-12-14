from pyrover import CLItxt
from pyrover import Grid

MAX_GRID_SIZE = 100


class Main():
    def __init__(self):
        self.cli = CLItxt(MAX_GRID_SIZE)
        self.grid = Grid(self.cli.grid_size[0], self.cli.grid_size[1], 1)

    def run(self):
        print(self.cli.grid_size)
        print(self.cli.start_pos)
        print(self.cli.commands)
        self.grid.print_as_grid()


if __name__ == "__main__":
    main = Main()
    main.run()
