from math import inf
from queue import PriorityQueue

with open("matrix.txt", "r") as f:
	matrix = f.readlines()
grid = [[int(num) for num in line.replace("\n", "").split(",")] for line in matrix]
size = len(grid)
grid = {(y, x) : grid[x][y] for x in range(len(grid)) for y in range(len(grid))}

ds = []
for row in range(size):
	v = (0, row)
	distances = {}
	distances[v] = grid[v]
	visited = set()

	queue = PriorityQueue()
	while len(distances) < len(grid):
		for dx, dy in [(0, 1), (0, -1), (1, 0)]:
			w = (v[0]+dx, v[1]+dy)
			if w not in visited and w in grid:
				d = distances[v] + grid[w]
				if d < distances.get(w, inf):
					distances[w] = d
					queue.put((d, w))
		visited.add(v)
		while True:
			_, v = queue.get()
			if v not in visited:
				break
	min_d = min([distances[(size-1, row)] for row in range(size)])
	ds.append(min_d)
print(min(ds))

		