import random

def start_game():

    grid = []

    for _ in range(4):
        grid.append([0] * 4)

    print('''Commands are as follows:
    'W' or 'w' : Move Up 
    'A' or 'a' : Move Left
    'S' or 's' : Move Down
    'D' or 'd' : Move Right
''')

    add_new_2(grid)
    return grid

def add_new_2(grid):
    random_number = [2,4,6,8]

    r = random.randint(0, 3)
    c = random.randint(0, 3)

    if grid[r] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)


        for i in range(4):
            for j in range(4):
                if grid[r][c] == 0 and grid[i][j] < 4:
                    grid[r][c] = 2
                elif grid[r][c] == 0 and (grid[i][j] >= 16 and grid[i][j] < 32) :
                    print('Nicely done!')
                    grid[r][c] = 4
                elif grid[r][c] == 0 and grid[i][j] >= 32:
                    print('Perfect!!')
                    grid[r][c] = random.choice(random_number)
                    
    return grid
def get_current_state(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return 'Congratulations!! You won!!'

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0 :
                return 'GAME NOT OVER'

    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i][j+1]:
                return 'GAME NOT OVER'

    for j in range(3):
        if grid[3][j] == grid[3][j+1] and grid[j][3] == grid[j+1][3]:
            return 'GAME NOT OVER'

    return 'You lost'


def compress(grid):
    changed = False

    new_grid = []

    for _ in range(4):
        new_grid.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]

                if j != pos:
                    changed = True
                pos += 1

    return new_grid, changed


def merged(grid):
    changed = False

    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0 
                
                changed = True

    return grid, changed


def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3 - j])

    return new_grid


def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i]) 
    return new_grid


def move_left(grid): 
    new_grid, changed1 = compress(grid)

    new_grid, changed2 = merged(new_grid)

    change = changed1 or changed2

    new_grid, _ = compress(new_grid)

    return new_grid, change


def move_right(grid):
    new_grid = reverse(grid) 

    new_grid, changed = move_left(new_grid)

    new_grid = reverse(new_grid)
    return new_grid, changed


def move_up(grid):
    new_grid = transpose(grid)

    new_grid, changed = move_left(new_grid)

    new_grid = transpose(new_grid)

    return new_grid, changed


def move_down(grid):
    new_grid = transpose(grid)

    new_grid, changed = move_right(new_grid)

    new_grid = transpose(new_grid)

    return new_grid, changed
