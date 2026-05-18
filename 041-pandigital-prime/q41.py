n = 10**8
primes = [True]*n
primes[0] = False
primes[1] = False
list_of_primes = [2]

for num in range(3, n+1, 2):
    if primes[num]:
        list_of_primes.append(num)
        for i in range(num**2, n, num):
            primes[i] = False

def is_pandigital(num):
    for i in range(1, len(num)+1):
        if str(i) not in num:
            return False
    return True

print("stage 2")
largest = 0
for prime in list_of_primes:
    if is_pandigital(str(prime)):
        largest = max(prime, largest)
print(largest)