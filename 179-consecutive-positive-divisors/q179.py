from math import sqrt

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

ps = primes(10**7)
is_prime = lambda n : n in ps
cache = {}

def join_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1: d1[k] += v
        else: d1[k] = v
    return d1

def dpf(num):
    orig_num = num
    factors = {}
    while num % 2 == 0:
        num //= 2
        if 2 not in factors: factors[2] = 1
        else: factors[2] += 1
    for factor in range(3, int(sqrt(num))+1, 2):
        if num in cache: 
            cache[orig_num] = join_dicts(factors, cache[num])
            return cache[orig_num]
        while num % factor == 0:
            if factor not in factors: factors[factor] = 1
            else: factors[factor] += 1
            num //= factor
    if num > 2: factors[num] = 1
    cache[orig_num] = factors
    return factors

def num_divisors(num):
    product = 1
    for power in dpf(num).values():
        product *= power + 1
    return product

cache2 = {}
total = 0
for n in range(2, 10**7):
    if not (is_prime(n) ^ is_prime(n+1)):
        d1 = cache2[n] if n in cache2 else num_divisors(n)
        d2 = cache2[n+1] if n+1 in cache2 else num_divisors(n+1)
        cache2[n] = d1
        cache2[n+1] = d2
        if d1 == d2:
            print(n)
            total += 1
print(total)
