n = 2000000
primes = [True]*n
primes[0] = False
primes[1] = False
list_of_primes = [2]

for num in range(3, n+1, 2):
    if primes[num]:
        list_of_primes.append(num)
        for i in range(num**2, n, num):
            primes[i] = False

print(len(list_of_primes))
print(list_of_primes[-1])
print(sum(list_of_primes))
# print(list_of_primes[10000])
# print(list_of_primes)
