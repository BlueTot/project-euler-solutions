from itertools import permutations

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

big_ps = primes(100000000)
def is_valid(ps):
    for p in permutations(list(map(str, ps)), 2):
        if int(p[0]+p[1]) not in big_ps:
            return False
    return True
            

def recurse(answer=[]):
    print(answer)
    if len(answer) == 5:
        print(answer)
        print(sum(answer))
        
    for p in primes(10000):
        if is_valid(answer + [p]):
            recurse(answer + [p])

recurse()
