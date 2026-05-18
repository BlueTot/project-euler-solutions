from math import sqrt

def dpf(num):
    factors = set()
    while num % 2 == 0:
        num //= 2
        factors.add(2)
    for factor in range(3, int(sqrt(num))+1, 2):
        while num % factor == 0:
            factors.add(factor)
            num //= factor
    if num > 2:
        factors.add(num)
    return factors

def totient(n):
    product = n
    for num in dpf(n):
        product *= 1 - 1/num
    return round(product)

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

total = 0
cache = {1:0}
for p in primes(4*10**7):
    print(p)
    curr, length = p, 1
    while True:
        curr = totient(curr)
        if curr in cache:
            length += cache[curr]
            break
        length += 1
    cache[p] = length
    if length == 25:
        total += p
print(total)
    