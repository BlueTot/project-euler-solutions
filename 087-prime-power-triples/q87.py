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

ps = primes(8000)
nums = set()
for p1 in ps:
    print(p1)
    for p2 in ps:
        for p3 in ps:
            num = p1**2 + p2 **3 + p3 **4
            if num < 5 * 10**7: nums.add(num)
print(len(nums))
# print(nums)
