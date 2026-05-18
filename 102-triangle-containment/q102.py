def det(u, v):
    return u[0]*v[1] - u[1]*v[0]

def in_triangle(a, b, c, v):
    v0 = a
    v1 = (b[0]-v0[0], b[1]-v0[1])
    v2 = (c[0]-v0[0], c[1]-v0[1])
    a = (det(v, v2) - det(v0, v2))/det(v1, v2)
    b = -(det(v, v1) - det(v0, v1)) / det(v1, v2)
    return a > 0 and b > 0 and a + b < 1

with open("triangles.txt", "r") as f:
    triangles = [list(map(int, line.replace(" ", "").split(","))) for line in f.readlines()]

total = 0
for line in triangles:
    a = (line[0], line[1])
    b = (line[2], line[3])
    c = (line[4], line[5])
    if in_triangle(a, b, c, (0, 0)):
        total += 1
print(total)



