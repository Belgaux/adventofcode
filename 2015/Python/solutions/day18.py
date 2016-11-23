import copy

ON = "#"
OFF = "."

def show_grid(grid):
    for row in grid:
        for elem in row:
            print(elem, end="")
        print()
    print()

def pad_array(arr):
    """Create a padded array for easier neighbor checking
    """
    pad = [OFF] * (len(arr) + 2)
    padded = [[OFF] + row + [OFF] for row in arr]
    padded.insert(0, pad)
    padded.append(pad)
    return padded

def neighbor_count(row, col, grid):
    """Count number of adjacent cells that are on
    """
    count = 0
    # iterate the Moore neighborhood
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if grid[i][j] == ON and not (i == row and j == col):
                count += 1
    return count

def get_next_grid(grid):
    """Update the grid logic (Game of Life)
    """
    # deepcopy to preserve state
    next_grid = copy.deepcopy(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            cell = grid[i][j]
            if cell == OFF and neighbor_count(i, j, grid) == 3:
                next_grid[i][j] = ON
            elif cell == ON and neighbor_count(i, j, grid) not in [2, 3]:
                next_grid[i][j] = OFF
    return next_grid

def add_corners(grid):
    """Add fixed corners for part 2 (taking into account padding)
    """
    grid[1][1] = ON
    grid[1][100] = ON
    grid[100][1] = ON
    grid[100][100] = ON

def main():
    in_file = [line.strip() for line in \
            open("../inputs/input18.txt").readlines()]

    # setup inital state
    grid = [[OFF] * len(line) for line in in_file]
    for i, row in enumerate(in_file):
        for j, col in enumerate(row):
            grid[i][j] = col

    # animate
    grid = pad_array(grid)
    add_corners(grid)
    for _ in range(100):
        grid = get_next_grid(grid)
        add_corners(grid)
        #show_grid(grid)

    # count cells that are on
    print(len([elem for row in grid for elem in row if elem == ON]))


if __name__ == "__main__":
    main()
