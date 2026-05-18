from math import gcd

numfracs = 0
for d in range(2, 12001):
    for n in range(1, d):
        if 1/3 < n/d < 1/2 and gcd(n, d) == 1:
            numfracs += 1
    print(d)
print(numfracs)
