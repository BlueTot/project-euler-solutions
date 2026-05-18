n = 10**6
primes = [True]*n
primes[0] = False
primes[1] = False
list_of_primes = [2]

for num in range(3, n+1, 2):
    if primes[num]:
        list_of_primes.append(num)
        for i in range(num**2, n, num):
            primes[i] = False

def is_truncatable_prime(prime):
    #left
    p1 = str(prime)
    while len(p1) >= 1:
        if int(p1) not in list_of_primes:
            return False
        p1 = p1[1:]
    p2 = str(prime)
    while len(p2) >= 1:
        if int(p2) not in list_of_primes:
            return False
        p2 = p2[:-1]
    return True

tprimes = set()
for prime in list_of_primes:
    if is_truncatable_prime(prime) and prime not in [2, 3, 5, 7]:
        print(prime)
        tprimes.add(prime)
print(len(tprimes), sum(tprimes))
    
