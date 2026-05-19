#!/bin/python3


def euler11(grid: list[list[int]]) -> int:

    maxp = 1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= row - 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row-1][col]*grid[row-2][col]*grid[row-3][col])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= row + 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= col - 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row][col-1]*grid[row][col-2]*grid[row][col-3])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= col + 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row][col+1]*grid[row][col+2]*grid[row][col+3])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= row + 3 <= 19 and 0 <= col + 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= row + 3 <= 19 and 0 <= col - 3 <= 19:
                maxp = max(maxp, grid[row][col]*grid[row+1][col-1]*grid[row+2][col-2]*grid[row+3][col-3])

    return maxp


grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

print(euler11(grid))
