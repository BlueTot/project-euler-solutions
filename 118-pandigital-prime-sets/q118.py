from functools import lru_cache

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

def is_prime(s):
    if s == "": return False
    return int(s) in ps

outputs = []

@lru_cache
def num_ways(digits=(1, 2, 3, 4, 5, 6, 7, 8, 9), groups=tuple()):
    global outputs
    if len(digits) == 0:
        if is_prime(int(list(groups)[-1])) or (int(list(groups)[-1]) > 10**8 and int(list(groups)[-1]) % 2 == 1):
            outputs.append(str(sorted([int(i) for i in groups])))
            return 1
    digits_set = set(digits)
    ways = 0
    for digit_to_remove in digits:
        # start a new group
        if groups:
            if is_prime(list(groups)[-1]): # check if current group is prime
                digits_set.remove(digit_to_remove) # remove from digits
                ways += num_ways(tuple(sorted(digits_set)), tuple(list(groups) + [str(digit_to_remove)]))
                digits_set.add(digit_to_remove)
        else:
            digits_set.remove(digit_to_remove) # remove from digits
            ways += num_ways(tuple(sorted(digits_set)), tuple(list(groups) + [str(digit_to_remove)]))
            digits_set.add(digit_to_remove)
        # or continue the group
        if groups:
            digits_set.remove(digit_to_remove)
            ways += num_ways(tuple(sorted(digits_set)), tuple(list(groups)[:-1] + [list(groups)[-1] + str(digit_to_remove)]))
            digits_set.add(digit_to_remove)
    return ways

print(num_ways())  
with open("data.txt", "w") as f:
    f.writelines("\n".join(outputs))
            
        
        