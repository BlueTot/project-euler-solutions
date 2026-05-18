from ast import literal_eval

with open("data.txt", "r") as f:
    data = f.read().split("\n")

def isp(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

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

ps = primes(10**8)
print("done part 1")

def is_prime(n):
    if n > 10**8:
        return isp(n)
    return n in ps

nums = set()
for idx, i in enumerate(data):
    print(idx)
    row = literal_eval(i)
    for num in row:
        if not is_prime(num):
            break
    else:
        nums.add(tuple(row))
print(len(nums))

