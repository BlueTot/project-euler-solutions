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

for num in range(3, n+1, 2):
    if num not in list_of_primes:
        success = True
        for p in list_of_primes:

            rem = (num - p)

            if rem < 0:
                break

            if rem % 2 != 0:
                continue

            rem = rem // 2
            if int(rem ** 0.5) ** 2 == rem:
                success = False
                break
            
        if success:
            print(num)
            break
    print(num)