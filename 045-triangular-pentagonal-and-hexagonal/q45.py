def triangulars(n):
    tris = set()
    for i in range(1,n+1):
        tris.add(i*(i+1)//2)
    return tris

def pentagonals(n):
    pents = set()
    for i in range(1, n+1):
        pents.add(i*(3*i-1)//2)
    return pents

def hexagonals(n):
    hexs = set()
    for i in range(1, n+1):
        hexs.add(i*(2*i-1))
    return hexs

n=100000
tris = triangulars(n)
pents = pentagonals(n)
hexs = hexagonals(n)

print(tris & pents & hexs)