from math import inf
target = 2000000
min_diff = inf
outputx, outputy = 0, 0

for x in range(3000):
    for y in range(3000):
        area = 1/4 * x * y * (x + 1) * (y + 1)
        diff = abs(area - target)
        if diff < min_diff:
            outputx, outputy = x, y
            min_diff = diff
print(outputx, outputy, outputx*outputy)


