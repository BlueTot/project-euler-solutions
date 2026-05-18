from math import factorial

def combination(n, r):
    return factorial(n)/(factorial(r) * factorial(n-r))

vals = 0
nrs = set()
for n in range(1, 101):
    for r in range(1, n):
        if combination(n, r) > 10**6:
            vals += 1
            nrs.add((n, r))
print(vals)
print(nrs)