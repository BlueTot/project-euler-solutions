def pentagonals(n):
    pents = set()
    for i in range(1, n+1):
        pents.add(i*(3*i-1)//2)
    return pents

print(pentagonals(100))

pents = pentagonals(10000)

ds = []
for pent1 in pents:
    for pent2 in pents:
        if (pent1 + pent2) in pents and abs(pent2 - pent1) in pents:
            ds.append(abs(pent2-pent1))
            print(pent1, pent2)

print(ds)
# print(min(ds))