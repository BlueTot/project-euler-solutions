def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = []
    list_of_primes.append(2)

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.append(num)
            for i in range(num**2, n, num):
                primes[i] = False

    return list_of_primes

def divisors(num):
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0 and factor != num:
            yield factor, num//factor

N = 10**8
vals = set()
ps = primes(N)
ps_set = set(ps)
for item in ps:
    num = item - 1
    for d1, d2 in divisors(num):
        if d1+d2 not in ps_set:
            break
    else:
        vals.add(num)
        print(num)

print(sum(vals))
