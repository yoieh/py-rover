import pytest
from pyrover import Rover
from pyrover import Grid


def test_rover_init():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    assert rover.grid == grid
    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == "N"
    assert rover.moves == [[0, 0, "N"]]
    assert rover.commands == []


def test_rover_take_input():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    commands = ["L", "M", "R"]
    rover.take_input(commands)
    assert rover.commands == ["L", "M", "R"]


def test_rover_take_input_invalid_command():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    commands = ["L", "M", "R", "A"]
    with pytest.raises(ValueError):
        rover.take_input(commands)


def test_rover_move():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    rover.move()
    assert rover.y == 1
    assert rover.moves == [[0, 0, "N"], [0, 1, "N"]]


def test_rover_trun_left():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    rover.turn_left()
    assert rover.direction == "W"
    assert rover.moves == [[0, 0, "N"], [0, 0, "W"]]


def test_rover_trun_right():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    rover.turn_right()
    assert rover.direction == "E"
    assert rover.moves == [[0, 0, "N"], [0, 0, "E"]]


def test_rover_check_obstacle():
    grid = Grid(5, 5)
    grid.grid = [1, 0, 0, 0, 0]
    rover = Rover(grid, 0, 0, "N")
    assert rover.check_obstacle(0, 0) == True


def test_rover_check_out_of_bounds():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    assert rover.check_out_of_bounds(-1, 0) == True


def test_rover_get_last_position():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, "N")
    rover.take_input(["L", "M", "R"])
    assert rover.get_last_position() == [0, 0, "N"]


def test_rover_fell_off():
    grid = Grid(1, 1)
    rover = Rover(grid, 0, 0, "N")
    rover.take_input(["M", "M"])

    with pytest.raises(ValueError):
        for comand in rover.commands:
            rover.handel_command(comand)

    assert rover.fell_off_grid == True


def test_rover_stuck():
    grid = Grid(5, 5)
    for i in range(len(grid.grid)):
        grid.grid[i] = 1

    grid.grid[i] = 0

    rover = Rover(grid, 0, 0, "N")
    rover.take_input(["M", "M"])

    with pytest.raises(ValueError):
        for comand in rover.commands:
            rover.handel_command(comand)

    assert rover.stuck == True
