from fractions import Fraction

N = 18
circuits = [set() for _ in range(N+1)]
circuits[1].add(60)
for n in range(2, N+1):
    for a in range(1, n):
        print(n, a)
        for c1 in circuits[a]:
            for c2 in circuits[n-a]:
                circuits[n].add(Fraction(c1 + c2))
                circuits[n].add(Fraction((c1 * c2) / (c1 + c2)))
print(len(set.union(*circuits)))
