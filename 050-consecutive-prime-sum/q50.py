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

largest_p = 0
largest_length = 0
lengths = {}
for p in list_of_primes:
    found = False
    for startidx in range(len(list_of_primes)):
        total = 0
        numterms = 0
        if found:
            break
        if list_of_primes[startidx] > p:
            break
        for idx in range(startidx, len(list_of_primes)):
            total += list_of_primes[idx]
            numterms += 1
            if total == p:
                lengths[p] = numterms
                found = True
                break
            if total > p:
                break
    if lengths[p] > largest_length:
        largest_length = lengths[p]
        largest_p = p
    print(p)
print(largest_p, largest_length)
                