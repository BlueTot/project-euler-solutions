from collections import Counter

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = set()
    list_of_primes.add(2)

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.add(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

ps = primes(10**6)

def replacements(p):
    digits = Counter([i for i in str(p)]).keys()
    for d in digits:
        for rd in [str(i) for i in range(10)]:
            n = str(p).replace(d, rd)
            if len(str(int(n))) == len(str(p)):
                yield int(n), d

for p in ps: 
    totals = {}
    for replacement, d in replacements(p):
        if replacement in ps:
            if d not in totals:
                totals[d] = 0
            totals[d] += 1
    if 8 in totals.values():
        print(p)
