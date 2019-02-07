import random
import time
import numpy as np

def new_game(grid_num):
    print("A new Board is initialized!")
    grid = []
    for i in range(grid_num):
        grid.append( grid_num * [0])
    grid = add_two_to_grid(grid)
    grid = add_two_to_grid(grid)
    # print(grid)
    return grid

def add_two_to_grid(grid):
    if min(list(map(min, zip(*grid))))> 0:
        print("Board is full after this op!")
        return grid
    random.seed(time.time())
    x, y = random.randint(0,len(grid)-1), random.randint(0, len(grid)-1)
    while grid[x][y] != 0:
        x, y = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
    grid[x][y] = 2
    return grid

# only process a horizontal line and swipe right,
# other cases can be converted to this case
# using a queue to process this

def update_grid_line(grid_line):
    grid_length = len(grid_line)
    remove_zero = [x for x in grid_line if x != 0]
    new_line = []
    cnt = 0
    score_got = 0
    while len(remove_zero) > 1:
        cnt += 1
        if cnt > 10:
            return grid_line
        value1 = remove_zero.pop()
        value2 = remove_zero.pop()
        if value1 == value2:
            new_line.insert(0, value1*2)
            score_got += int(value1)
        else:
            new_line.insert(0, value1)
            remove_zero.append(value2)
    new_line = remove_zero + new_line
    new_line = (grid_length - len(new_line)) * [0] + new_line
    return new_line, score_got


def update_grid(grid,key_pressed):
    score_got = 0
    # print(grid)
    if key_pressed == "right":
        for i in range(len(grid)):
            grid[i], score_line = update_grid_line(grid[i])
            score_got += score_line

    elif key_pressed == "left":
        for i in range(len(grid)):
            reversed_grid = grid[i][::-1]
            grid[i], score_line = update_grid_line(reversed_grid)
            grid[i].reverse()
            score_got += score_line

    elif key_pressed == "up":
        rot_right = np.rot90(np.array(grid), k = -1)
        for i in range(len(grid)):
            rot_right[i], score_line = update_grid_line(rot_right[i])
            score_got += score_line
        grid = np.rot90(rot_right).tolist()

    elif key_pressed == "down":
        rot_right = np.rot90(np.array(grid))
        for i in range(len(grid)):
            rot_right[i], score_line = update_grid_line(rot_right[i])
            score_got += score_line
        grid = np.rot90(rot_right,k = -1).tolist()

    grid = add_two_to_grid(grid)
    return grid, score_got

def game_state(grid):
    # winning situation
    if max(list(map(max, zip(*grid)))) == 2048:
        print("Got 2048, Won!")
        return "win"

    # now checking for lose situation
    # if the grid is not full, then not lose
    if min(list(map(min,zip(*grid)))) == 0:
        return

    # dfs to check if there are adjacent equal number
    # if so, not lost
    for x in range(len(grid)):
        for y in range(len(grid)):
            if x != len(grid)-1 and grid[x][y] == grid[x+1][y]:
                return
            if y != len(grid)-1 and grid[x][y] == grid[x][y+1]:
                return

    print(" no way to go, lost this game")
    return "lose"
