n = 150000
primes = [True]*n
primes[0] = False
primes[1] = False
list_of_primes = [2]

for num in range(3, n+1, 2):
    if primes[num]:
        list_of_primes.append(num)
        for i in range(num**2, n, num):
            primes[i] = False

def dpf(num):
    factors = set()
    while num > 1:
        for factor in range(2, num+1):
            if num % factor == 0:
                factors.add(factor)
                num //= factor
                break
    return factors

for num in range(1, n+1):
    if num not in list_of_primes:
        if len(dpf(num)) == 4:
            if len(dpf(num+1)) == 4:
                if len(dpf(num+2)) == 4:
                    if len(dpf(num+3)) == 4:
                        print(num, num+1, num+2, num+3)
                        break
    if num % 1000 == 0:
        print(num)


