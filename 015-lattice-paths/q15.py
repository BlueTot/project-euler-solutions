# start = (1, 0)
# gridsize = 8
# n = 0
# def recurse(node):
#     global n
#     if node == (gridsize, gridsize):
#         n += 2
#         return
#     for dx, dy in ((1, 0), (0, 1)):
#         x = node[0] + dx
#         y = node[1] + dy
#         if 0 <= x <= gridsize and 0 <= y <= gridsize:
#             recurse((x, y))
# recurse(start)
# print(n)

#6
#20
#70
#252
#924
#3432
#12870

from math import factorial

from math import comb

def ways(n):
    return comb(n*2, n)

print([ways(i) for i in  range(2, 21)])