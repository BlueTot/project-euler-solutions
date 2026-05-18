from math import log10

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = [2]

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.append(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

ps = primes(10**5)
const = 800800 * log10(800800)
total = 0
seen = set()
for p in ps:
    print(p)
    for q in ps:
        if p != q:
            if (n := q*log10(p) + p*log10(q)) <= const:
                if n not in seen:
                    total += 1
                seen.add(n)
            else:
                break
print(total)

'''
result for 100k:
45998435

45998435

largest n found is 1M, largest n needed is over 4M
'''

