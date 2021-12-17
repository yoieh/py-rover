from os import system
from pyrover.Grid import Grid


class Rover:
    def __init__(self, grid, x, y, direction):
        self.grid: Grid = grid
        self.x = x
        self.y = y
        self.direction = direction
        self.moves = [[x, y, direction]]
        self.commands = []

        self.stuck = False
        self.fell_off_grid = False

    def take_input(self, commands):
        # validate commands
        for command in commands:
            if command not in ["L", "M", "R"]:
                raise ValueError("Invalid command")

        self.commands = commands

    def run(self):
        for command in self.commands:
            self.handel_command(command)

    def handel_command(self, command):
        if command == "M":
            x, y = self.next_position(self.x, self.y, self.direction)

            if self.check_out_of_bounds(x, y) != False:
                self.fell_off_grid = True
                raise ValueError("Out of bounds")
            if self.check_obstacle(x, y) != False:
                self.stuck = True
                raise ValueError("Obstacle detected")

            self.move()

        elif command == "L":
            self.turn_left()
        elif command == "R":
            self.turn_right()

    def next_position(self, x, y, direction):
        if direction == "N":
            y += 1
        elif direction == "E":
            x += 1
        elif direction == "S":
            y -= 1
        elif direction == "W":
            x -= 1
        return x, y

    def move(self):
        self.x, self.y = self.next_position(self.x, self.y, self.direction)
        self.moves.append([self.x, self.y, self.direction])

    def next_left_direction(self, direction):
        if direction == "N":
            return "W"
        elif direction == "E":
            return "N"
        elif direction == "S":
            return "E"
        elif direction == "W":
            return "S"

    def turn_left(self):
        self.direction = self.next_left_direction(self.direction)
        self.moves.append([self.x, self.y, self.direction])

    def next_right_direction(self, direction):
        if direction == "N":
            return "E"
        elif direction == "E":
            return "S"
        elif direction == "S":
            return "W"
        elif direction == "W":
            return "N"

    def turn_right(self):
        self.direction = self.next_right_direction(self.direction)
        self.moves.append([self.x, self.y, self.direction])

    def check_obstacle(self, x, y):
        cell = self.grid.get_cell(x, y)

        if cell >= 1 or cell < 0:
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

    def get_last_position(self):
        return self.moves[len(self.moves) - 1]
