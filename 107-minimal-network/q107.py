from math import inf
from collections import deque

with open("networktest.txt") as f:
    data = [[int(i) if i != "-" else inf for i in line.split(",")] for line in f.read().split("\n")]
    matrix = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] != inf:
                matrix.append((row, col, data[row][col]))

def has_cycle(graph):
    queue = deque([list(graph.keys())[0]])
    visited = set()
    edges = set()
    while queue:
        v = queue.popleft()
        if v in visited: return True
        visited.add(v)
        for w in graph[v]:
            if w not in visited and (v, w) not in edges:
                queue.append(w)
                edges.add((v, w))
                edges.add((w, v))
            elif w in visited and (v, w) not in edges:
                return True
    return False

matrix = sorted(matrix, key=lambda node : node[2])

graph = {i : set() for i in range(len(data))}
edges = set()
total_edges = set()
for v, w, weight in matrix:
    if w in graph[v] and v in graph[w]:
        continue
    graph[v].add(w)
    graph[w].add(v)
    if has_cycle(graph):
        graph[v].remove(w)
        graph[w].remove(v)
    else:
        edges.add((v, w, weight))
    a, b = min(v, w), max(v, w)
    total_edges.add((a, b, weight))

new_weight = sum([n[2] for n in edges])
orig_weight = sum([n[2] for n in total_edges])
print(orig_weight - new_weight)
