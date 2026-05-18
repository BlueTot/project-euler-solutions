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

def factorisation(num):
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