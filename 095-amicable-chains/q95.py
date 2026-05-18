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

ps = primes(10**6)
is_prime = lambda n : n in ps

def _d(num):
    if is_prime(num):
        return 1
    factors = []
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0 and factor != num:
            factors.append(factor)
            if factor != num / factor and num//factor != num:
                factors.append(num//factor)
    return sum(factors)

cache = {}

def d(num):
    global cache
    if num in cache:
        return cache[num]
    cache[num] = _d(num)
    return cache[num]

longest_length, N, smallest, largest = 0, 0, 0, 0

for n in range(1, 10**5):
    curr, stack = n, set()
    valid = False
    while True:
        prev = curr
        curr = d(curr)
        if len(stack) > 0 and max(stack) > 10**6: break
        if curr == 0: break
        if curr == n:
            valid = True
            break
        if curr in stack and curr != n: break
        stack.add(curr)
    if valid and len(stack) > longest_length and max(stack) <= 10**6:
        longest_length = len(stack)
        N = n
        smallest = min(min(stack), N)
        largest = max(max(stack), N)
        print(longest_length, N, smallest, largest)
print(longest_length, N, smallest, largest)
