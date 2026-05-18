from math import sqrt

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

ps = primes(10**6)
is_prime = lambda n : n in ps

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

def R(d):
    return totient(d) / (d-1)

ratio = 15499/94744

def run():
    idx = 0
    n = ps[0]
    while n < 10**9:
        print(idx)
        if idx != 0: n *= ps[idx]
        for k in range(1, ps[idx+1]):
            d = n*k
            r = R(d)
            if r < ratio:
                print(d)
                return
        idx += 1
            
if __name__ in "__main__":
    run()
