from copy import deepcopy

def load_file():
    with open("sudoku.txt", "r") as f:
        sudoku = f.readlines()
    grid = [[]]
    count = 0
    for line in sudoku:
        if line[0] == "G":
            continue
        grid[-1].append([int(digit) for digit in line.replace("\n", "")])
        count += 1
        if count == 9:
            count = 0
            grid.append([])
    return grid[:-1]

def in_row(grid, row, num):
    return num in grid[row]

def in_col(grid, col, num):
    return num in [row[col] for row in grid]

def in_3x3_matrix(board, row, col, num):
    curr_box = (row // 3, col // 3)
    box = []
    for row in range(3*curr_box[0], 3*(curr_box[0] + 1)):
        for col in range(3*curr_box[1], 3*(curr_box[1]+1)):
            box.append(board[row][col])
    return num in box

def is_safe(grid, row, col, num):
    return (not in_row(grid, row, num)) and (not in_col(grid, col, num)) and (not in_3x3_matrix(grid, row, col, num))

def next_available_square(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)

def print_board(board):
    for row in range(len(board)):
        for col in range(len(board)):
            print(board[row][col], end=' ')
        print()
    print()

def solve_sudoku(board, row=0, col=0):

    if col == 9 and row == 8:
        return True
    
    if col == 9:
        col = 0
        row += 1
    
    if board[row][col] > 0:
        return solve_sudoku(board, row, col+1)
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, row, col+1):
                return True
        board[row][col] = 0

    return False

puzzles = load_file()
total = 0
for idx, puzzle in enumerate(puzzles):
    print(idx+1)
    new_puzzle = deepcopy(puzzle)
    if solve_sudoku(new_puzzle):
        print(new_puzzle)
        total += int(str(new_puzzle[0][0])+str(new_puzzle[0][1])+str(new_puzzle[0][2]))
print(total)
        