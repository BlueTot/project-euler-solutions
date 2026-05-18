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

ps = primes(1000)
n = 2
while True:
    lst = [1]+[0]*(n)
    for p in ps:
        for num in range(p, n+1):
            if 0 <= num - p <= num:
                lst[num] += lst[num-p]
    print(n, lst[n])
    if lst[n] > 5000:
        print(n)
        break
    n += 1
