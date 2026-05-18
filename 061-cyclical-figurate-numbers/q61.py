def triangle(n):
    return int(n*(n+1)//2)

def square(n):
    return int(n**2)

def pentagon(n):
    return int(n*(3*n-1)//2)

def hexagon(n):
    return int(n*(2*n-1))

def heptagon(n):
    return int(n*(5*n-3)//2)

def octagon(n):
    return int(n*(3*n-2))

P3 = set([triangle(n) for n in range(1, 1000) if len(str(triangle(n))) == 4])
P4 = set([square(n) for n in range(1, 1000) if len(str(square(n))) == 4])
P5 = set([pentagon(n) for n in range(1, 1000) if len(str(pentagon(n))) == 4])
P6 = set([hexagon(n) for n in range(1, 1000) if len(str(hexagon(n))) == 4])
P7 = set([heptagon(n) for n in range(1, 1000) if len(str(heptagon(n))) == 4])
P8 = set([octagon(n) for n in range(1, 1000) if len(str(octagon(n))) == 4])

from collections import deque

nums = []
for figurate_set, n in [(P3, 3), (P4, 4), (P5, 5), (P6, 6), (P7, 7), (P8, 8)]:
    nums += [[(i, n)] for i in figurate_set]

queue = deque([])
for n in nums:
    queue.append(n)

found = False
while not found:

    stack = queue.popleft()
    print(stack)

    if len(stack) == 6:
        if str(stack[-1][0])[-2:] == str(stack[0][0])[:2]:
            print(stack)
            print(sum([i[0] for i in stack]))
            found = True

    visited_sets = set(i[1] for i in stack)
    for v in nums:
        num, home = v[0]
        if home not in visited_sets and str(stack[-1][0])[-2:] ==  str(num)[:2]:
            queue.append(stack + [(num, home)])
