from collections import defaultdict

with open("matrix.txt", "r") as f:
	matrix = f.readlines()
grid = [[int(num) for num in line.replace("\n", "").split(",")] for line in matrix]
# print(grid)

	
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not (row == 0 and col == 0):
            if col == 0: grid[row][col] += grid[row-1][col]
            elif row == 0: grid[row][col] += grid[row][col-1]
            else: grid[row][col] += min(grid[row][col-1], grid[row-1][col])

print(grid[-1][-1])