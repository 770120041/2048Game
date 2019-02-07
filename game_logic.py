import random
import time
def new_game(grid_num):

    grid = []
    for i in range(grid_num):
        grid.append( grid_num * [0])
    grid = add_two_to_grid(grid)
    grid = add_two_to_grid(grid)
    return grid

def add_two_to_grid(grid):
    random.seed(time.time())
    x,y = random.randint(0,len(grid)-1),random.randint(0,len(grid)-1)
    while grid[x][y] != 0:
        x, y = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
    grid[x][y] = 2
    return grid

def update_grid(grid,key_pressed):
    pass

def game_state(grid):
    pass
