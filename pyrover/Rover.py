class Rover:
    def __init__(self, grid, x, y, direction):
        self.grid = grid
        self.x = x
        self.y = y
        self.direction = direction
        self.path = []

        self.validate_rover_starting_position()

    def validate_rover_starting_position(self):
        if(self.check_out_of_bounds(self.x, self.y)):
            print("Rover: Cant start out side of grid, I will fall out!")
            exit(1)

        if(self.check_obstacle(self.x, self.y)):
            print("Rover: I cant start on a obstacle!")
            exit(1)

    def simulate_run_rover(self, commands):
        # first of get the end position
        self.calculated_end_position = self.calculate_end_position(commands)

        # check that end positions isent on obstacle
        if self.grid.grid[self.calculated_end_position[1] * self.grid.width + self.calculated_end_position[0]] == 1:
            print("Error: Rovers end positions is unreachable")
            exit(1)

        # then calculate the path
        self.calculate_path(commands)

    def run_rover(self):
        # run the rover
        self.run_rover_path()

        # check if rover is on the end position
        if self.x == self.calculated_end_position[0] and self.y == self.calculated_end_position[1] and self.direction == self.calculated_end_position[2]:
            print("Rover is on the end position" +
                  str(self.calculated_end_position))

    # runs the rover at calculated path
    def run_rover_path(self):
        print("\nRover: I will run!")
        for position in self.path:
            self.x = position[0]
            self.y = position[1]
            self.direction = position[2]
            print("Rover: new position ", self.x, self.y, self.direction)

    # simultas a move in the direction the rover is facing
    def simulate_move(self):
        new_position = [0, 0]

        if self.direction == 'N':
            new_position[1] = -1
        elif self.direction == 'E':
            new_position[0] = 1
        elif self.direction == 'S':
            new_position[1] = 1
        elif self.direction == 'W':
            new_position[0] = -1

        return new_position

    # simulates a turn left
    def simulate_turn_left(self):
        last_direction = self.get_last_position()[2]

        if last_direction == 'N':
            return 'W'
        elif last_direction == 'E':
            return 'N'
        elif last_direction == 'S':
            return 'E'
        elif last_direction == 'W':
            return 'S'

    # sumulates a turn right

    def simulate_turn_right(self):
        last_direction = self.get_last_position()[2]
        if last_direction == 'N':
            return 'E'
        elif last_direction == 'E':
            return 'S'
        elif last_direction == 'S':
            return 'W'
        elif last_direction == 'W':
            return 'N'

    # simulates a command and returns false if it failed
    def simulate_command(self, command):
        last_position = self.get_last_position()
        next_x = last_position[0]
        next_y = last_position[1]
        next_direction = last_position[2]

        if command == 'M':
            new_move = self.simulate_move()
            next_x += new_move[0]
            next_y += new_move[1]

            if(self.check_obstacle(next_x, next_y)):
                return False

            if(self.check_out_of_bounds(next_x, next_y)):
                print("Rover: I will fall out!")
                print(next_x, next_y, next_direction)
                return False

        elif command == 'L':
            next_direction = self.simulate_turn_left()
        elif command == 'R':
            next_direction = self.simulate_turn_right()
        else:
            print("Error: Invalid command")
            exit(1)

        self.path.append([next_x, next_y, next_direction])
        return True

    def check_obstacle(self, x, y):
        if self.grid.grid[y * self.grid.width + x] == 1:
            return True
        else:
            return False

    def check_out_of_bounds(self, x, y):
        if x < 0 or x > self.grid.width - 1:
            return True
        elif y < 0 or y > self.grid.height - 1:
            return True
        else:
            return False

    def calculate_end_position(self, commands):
        self.path = [[self.x, self.y, self.direction]]
        for command in commands:
            self.simulate_command(command)
        return self.get_last_position()

    def calculate_path(self, commands):
        self.path = [[self.x, self.y, self.direction]]
        for command in commands:
            if self.simulate_command(command) == False:
                # TODO: try to calculate a new path of commands
                # this i think is a bit to much for now i will just print and exit
                # self.recalculate_path(command)
                print("Rover: I will get stuck!")
                break

    def get_last_position(self):
        return self.path[len(self.path) - 1]
