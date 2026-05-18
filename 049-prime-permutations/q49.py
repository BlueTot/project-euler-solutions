
n = 10000
primes = [True]*n
primes[0] = False
primes[1] = False
list_of_primes = [2]

for num in range(3, n+1, 2):
    if primes[num]:
        list_of_primes.append(num)
        for i in range(num**2, n, num):
            primes[i] = False

def highest(n):
    origlst = [int(i) for i in str(n)]
    newlst = []
    while origlst:
        newlst.append(n := max(origlst))
        origlst.remove(n)
    return int("".join(list(map(str, newlst))))

baseprimes = {prime : highest(prime) for prime in list_of_primes if len(str(prime)) == 4}
orderedprimes = {perm: [p for p, h in baseprimes.items() if h == perm] for perm in baseprimes.values()}

for primes in orderedprimes.values():
    print(primes)
    if len(primes) > 2 and 1487 not in primes:
        diffs = {}
        for prime1 in primes:
            for prime2 in primes:
                if prime1 != prime2:
                    diff = prime2 - prime1
                    if diff > 0:
                        diffs[(prime1, prime2)] = diff
                    else:
                        diffs[(prime2, prime1)] = -diff
        print(diffs)
        val_found = None
        for diff in diffs.values():
            if list(diffs.values()).count(diff) >= 2:
                val_found = diff
        if val_found is not None:
            s = set()
            for p, d in diffs.items():
                if d == val_found:
                    s.add(p[0])
                    s.add(p[1])
            primes = sorted(list(s))
            if len(primes) == 3:
                print(primes)
                break
