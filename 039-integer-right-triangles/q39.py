sols = {}

for p in range(1, 1000+1):
    sols[p] = set()
    for a in range(1, p+1):
        for b in range(1, a):
            if int((a**2+b**2)**0.5) == (a**2+b**2)**0.5:
                c = (a**2+b**2)**0.5
                if a+b+c == p:
                    sols[p].add((int(a), int(b), int(c)))
    if p % 100 == 0:
        print(p)
# print(sols)

maxlen = 0
maxp = 0
v = 0
for p, vals in sols.items():
    if len(vals) > maxlen:
        maxp = p
        v = vals
        maxlen = len(vals)
print(v)
print(maxlen, maxp)