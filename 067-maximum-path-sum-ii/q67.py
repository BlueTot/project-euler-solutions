tri = [[int(x) for x in row.split(' ')] for row in open("triangle2.txt").readlines()]
print(tri)

maxRow = len(tri)-2
for row in range(maxRow, -1, -1):
    for col in range(row+1):
        tri[row][col] += max(tri[row+1][col], tri[row+1][col+1])    
print(tri[0][0])
