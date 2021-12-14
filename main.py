from pyrover import CLItxt


MAX_GRID_SIZE = 100


class Main():
    def __init__(self):
        self.cli = CLItxt(MAX_GRID_SIZE)

    def run(self):
        print(self.cli.grid_size)
        print(self.cli.start_pos)
        print(self.cli.commands)


if __name__ == "__main__":
    main = Main()
    main.run()
