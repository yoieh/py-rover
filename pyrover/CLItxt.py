class CLItxt:
    # Reads files input from data/input.txt file and converts it to commands
    def __init__(self, max_grid_size, filePath="data/input.txt"):
        self.max_grid_size = max_grid_size
        self.grid_size = []  # [x, y]
        self.start_pos = []  # [x, y, direction] direction: N, S, E, W
        self.commands = []  # [command 1, command 2, ...] command: L, R, M

        self.read_file(filePath)

    def read_file(self, filePath):
        file = open(filePath, "r")
        lines = file.readlines()

        # clean characters
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

        self.grid_size = lines[0].split(',')
        self.validates_grid_size()

        self.start_pos = lines[1].split(',')
        self.validates_start_pos()

        self.commands = lines[2].split(',')
        self.validates_commands()

        file.close()

    def validates_grid_size(self):
        # validate grid size
        if len(self.grid_size) != 2:
            print("Error: Grid size is not valid")
            exit(1)

        # makeing grid coordinates ints
        for i in range(len(self.grid_size)):
            self.grid_size[i] = int(self.grid_size[i])

        # validate grid size
        if self.grid_size[0] > self.max_grid_size or self.grid_size[1] > self.max_grid_size:
            print("Error: Grid size is too big")
            exit(1)

    def validates_start_pos(self):
        # validate start position
        if len(self.start_pos) != 3:
            print("Error: Start position is not valid")
            exit(1)

        # makeing start position coordinates ints
        for i in range(len(self.start_pos) - 1):
            self.start_pos[i] = int(self.start_pos[i])

        # validate that the start position is within the grid
        if self.start_pos[0] > self.grid_size[0] or self.start_pos[1] > self.grid_size[1]:
            print("Error: Start position is out of grid")
            exit(1)

        # validate start positions direction shold be N, S, E, W
        if self.start_pos[2] != 'N' and self.start_pos[2] != 'S' and self.start_pos[2] != 'E' and self.start_pos[2] != 'W':
            print("Error: Start position direction is not valid")
            exit(1)

    def validates_commands(self):
        # validate commands should only be L, R, M
        for i in range(len(self.commands)):
            if self.commands[i] != 'L' and self.commands[i] != 'R' and self.commands[i] != 'M':
                print("Error: Command is not valid")
                exit(1)
