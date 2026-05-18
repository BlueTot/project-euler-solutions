from math import factorial

def pascal(row, col):
    return factorial(row) // (factorial(col) * factorial(row - col))

coefficients = set()

for row in range(51):
    for col in range(1, row+1):
        coefficients.add(pascal(row, col))
# print(coefficients)

largest = max(coefficients)
# print(largest)

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

squares = [p**2 for p in primes(10**8)]

total = 0
for n in coefficients:
    print(n)
    for sq in squares:
        if n % sq == 0:
            break
    else:
        total += n
print(total)

    