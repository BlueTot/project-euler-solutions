from itertools import permutations

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

circular_primes = {k: False for k in list_of_primes}

def rotations(string):
    orig = string
    c = 0
    while True:
        if c == 0:
            yield orig
        else:
            string = string[-1] + string[0:-1]
            # print(string)
            if string == orig:
                break
            yield string
        c += 1

# print(circular_primes)

# print([i for i in rotations("31")])

count = 0
for prime in circular_primes:
    perms = []
    if not circular_primes[prime]:

        for num in rotations(str(prime)):
            # print(num)

            num = int(num)

            if num not in list_of_primes:
                break
            perms.append(num)

        else:
            # print(perms)
            for p in perms:
                circular_primes[p] = True
    count += 1
    print(count)
print(circular_primes)
            
print(list(circular_primes.values()).count(True))
