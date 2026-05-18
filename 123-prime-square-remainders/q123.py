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
    return sorted(list_of_primes)

for i in range(len(ps := primes(10**7))):
    print(i)
    if ps[i] == 2:
        r = 2
    else:
        r = (2*ps[i]*(i+1)) % (ps[i]**2)
    if r > 10 ** 10:
        print(i+1)
        print("finished")
        break
print("ran out")
