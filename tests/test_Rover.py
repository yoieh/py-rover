import pytest
from pyrover import Rover
from pyrover import Grid


def test_takes_input():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'N')

    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == 'N'


def test_can_start_from_any_position():
    grid = Grid(5, 5)
    rover = Rover(grid, 1, 2, 'S')

    assert rover.x == 1
    assert rover.y == 2
    assert rover.direction == 'S'


def test_cant_start_from_invalid_position():
    grid = Grid(5, 5)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        Rover(grid, -1, 0, 'N')
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_can_turn_left():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'N')
    rover.path = [(rover.x, rover.y, rover.direction)]

    assert rover.simulate_turn_left() == 'W'


def test_can_turn_right():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'N')
    rover.path = [(rover.x, rover.y, rover.direction)]

    assert rover.simulate_turn_right() == 'E'


def test_can_move_forward():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'S')
    rover.path = [(rover.x, rover.y, rover.direction)]

    assert rover.simulate_move() == [0, 1]


def test_check_out_of_bounds():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'N')
    rover.path = [(rover.x, rover.y, rover.direction)]

    assert rover.check_out_of_bounds(rover.x, rover.y + 1) == False


def test_check_not_out_of_bounds():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'S')
    rover.path = [(rover.x, rover.y, rover.direction)]

    assert rover.check_out_of_bounds(rover.x, rover.y - 1) == True


def test_will_fall_off_grid_when_moving_forward():
    grid = Grid(5, 5)
    rover = Rover(grid, 0, 0, 'N')
    rover.path = [(rover.x, rover.y, rover.direction)]
    command = 'M'
    
    assert rover.simulate_command(command) ==  False
    
