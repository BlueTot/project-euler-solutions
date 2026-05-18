n = 2*(10**6)
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

def num_consecutive_primes(a, b):
    n = 0
    while True:
        val = n**2 + a * n + b
        n += 1
        if val not in list_of_primes:
            return n

print("stage2")
maxab = (0, 0)
maxn = 0
for a in range(-999, 1000):
    for b in range(-1000, 1000+1):
        n = num_consecutive_primes(a, b)
        if n > maxn:
            maxn = n
            maxab = (a, b)
            print(maxn, maxab)
    print(a)
print(maxn, maxab, maxab[0]*maxab[1])
        
