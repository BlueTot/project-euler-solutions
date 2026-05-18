N = int(1.5*10**6)
pyths = set()
for m in range(1, 1000+1):
    for n in range(1, 1000+1):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        L = 2*m*(m+n)
        if a > 0 and b > 0 and c > 0 and a+b+c <= N:
            pyths.add((a, b, c))

pyths2 = set()
for a, b, c in pyths:
    for k in range(1, N//(a+b+c)+1):
        pyths2.add((a*k, b*k, c*k))

lengths = {}
for a, b, c in pyths2:
    L = a+b+c
    if L not in lengths:
        lengths[L] = set()
    lengths[L].add(tuple(sorted((a, b, c))))

total = 0
for L, triples in lengths.items():
    if len(triples) == 1:
        total += 1
print(total)
