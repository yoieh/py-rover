import pytest
from pyrover import CLItxt

MAX_GRID_SIZE = 100


def test_max_grid_size():
    cli = CLItxt(MAX_GRID_SIZE)
    assert cli.max_grid_size == MAX_GRID_SIZE


# test for an exit... should realy use exeptions and not exit codes
def test_exit_on_invalid_grid_size():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.grid_size = [MAX_GRID_SIZE + 1, 2]
        cli.validates_grid_size()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_exit_on_invalid_grid_size_input():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.grid_size = [1, 2, 3]
        cli.validates_grid_size()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_start_pos():
    cli = CLItxt(MAX_GRID_SIZE)
    cli.start_pos = [1, 2, 'N']
    assert cli.start_pos == [1, 2, 'N']


def test_exit_on_invalid_start_pos_x():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.start_pos = [MAX_GRID_SIZE + 1, 2, 'N']
        cli.validates_start_pos()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_exit_on_invalid_start_pos_direction():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.start_pos = [1, 2, 'A']
        cli.validates_start_pos()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_exit_on_invalid_start_pos_input():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.start_pos = [1, 2, 'N', 3]
        cli.validates_start_pos()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_commands():
    cli = CLItxt(MAX_GRID_SIZE)
    cli.commands = ['L', 'M', 'R', 'M', 'M']
    assert cli.commands == ['L', 'M', 'R', 'M', 'M']


def test_exit_on_invalid_commands():
    cli = CLItxt(MAX_GRID_SIZE)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli.commands = ['L', 'M', 'R', 'M', 'M', 'A']
        cli.validates_commands()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_read_file():
    cli = CLItxt(MAX_GRID_SIZE)
    cli.read_file('data/test_CLItxt.txt')
    assert cli.grid_size == [5, 5]
    assert cli.start_pos == [1, 2, 'N']
    assert cli.commands == ['L', 'M', 'R', 'M', 'M']
