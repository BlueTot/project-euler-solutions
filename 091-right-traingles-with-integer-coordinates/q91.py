from itertools import product

def dot(p, q):
    return p[0]*q[0]+p[1]*q[1]

n=50
visited = set()
for x1, y1 in product(range(n+1), repeat=2):
    for x2, y2 in product(range(n+1), repeat=2):
        if (x1, y1) != (0, 0) and (x2,  y2) != (0, 0) and (x1, y1) != (x2, y2):
            if dot((x1, y1), (x2, y2)) == 0 or dot((x2-x1, y2-y1), (x1, y1)) == 0 or dot((x2-x1, y2-y1), (x2, y2)) == 0:
                visited.add(tuple(sorted(((x1, y1), (x2, y2)))))
print(len(visited))
