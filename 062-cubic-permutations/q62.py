import math

def highest(cube):
    origlst = [int(i) for i in str(cube)]
    newlst = []
    while origlst:
        newlst.append(n := max(origlst))
        origlst.remove(n)
    return int("".join(list(map(str, newlst))))

def lowest(cube):
    origlst = [int(i) for i in str(cube)]
    newlst = []
    while origlst:
        newlst.append(n := min(origlst))
        origlst.remove(n)
    return int("".join(list(map(str, newlst))))

b = 0
while True:
    curr = b**3
    numperms = 0
    l, h = lowest(curr), highest(curr)
    perms = set()

    for base in range(math.floor(l**(1/3)), math.ceil(h**(1/3))+1):
        perm = base ** 3
        if highest(curr) == highest(perm):
            numperms += 1
            perms.add(perm)

    if numperms == 5:
        print(curr, perms, min(perms))
        break

    b += 1
    if curr % 100 == 0:
        print(curr, b)
    