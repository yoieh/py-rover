from pyrover import Grid


def test_grid_size():
    width = 5
    height = 5

    grid = Grid(width, height)
    assert grid.width == width
    assert grid.height == height


def test_create_grid():
    width = 10
    height = 5

    grid = Grid(width, height)
    assert len(grid.grid) == width*height


def test_generate_obstacles():
    obstacles = 4

    grid = Grid(5, 5, obstacles)

    count = 0
    for i in range(len(grid.grid)):
        if grid.grid[i] == 1:
            count += 1

    assert count <= obstacles
