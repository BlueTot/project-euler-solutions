# Num divisors

from math import sqrt

def prime_factorisation(num):
    factors = {}
    while num % 2 == 0:
        num //= 2
        if 2 not in factors:
            factors[2] = 1
        else:
            factors[2] += 1
    for factor in range(3, int(sqrt(num))+1, 2):
        while num % factor == 0:
            if factor not in factors:
                factors[factor] = 1
            else:
                factors[factor] += 1
            num //= factor
    if num > 2:
        factors[num] = 1
    return factors

cache = {}

def join_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1: d1[k] += v
        else: d1[k] = v
    return d1

def dpf(num):
    orig_num = num
    factors = {}
    while num % 2 == 0:
        num //= 2
        if 2 not in factors: factors[2] = 1
        else: factors[2] += 1
    for factor in range(3, int(sqrt(num))+1, 2):
        if num in cache: 
            cache[orig_num] = join_dicts(factors, cache[num])
            return cache[orig_num]
        while num % factor == 0:
            if factor not in factors: factors[factor] = 1
            else: factors[factor] += 1
            num //= factor
    if num > 2: factors[num] = 1
    cache[orig_num] = factors
    return factors

def num_divisors2(num2):
    product = 1
    for power in dpf(num2).values():
        product *= 2*power + 1
    return product

# main block of code

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = [2]

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.append(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

def num_sols(d):
    return (num_divisors2(d) + 1) // 2

def run():
    largest_n, largest_sols = 0, 0
    for n in range(1, 10**6):
        nsols = num_sols(n)
        if nsols > largest_sols:
            largest_sols = nsols
            largest_n = n
            print(largest_n, prime_factorisation(largest_n), largest_sols)

if __name__ in "__main__":
    run()


'''0
2 2
4 3
1
6 5
12 8
24 11
2
30 14
60 23
120 32
180 38
3
210 41
420 68
840 95
1260 113
1680 122
4
4620 203
9240 284
13860 338
18480 365
27720 473
5
60060 608
120120 851
180180 1013
240240 1094
360360 1418
6
1021020 1823
2042040 2552
3063060 3038
4084080 3281
6126120 4253
7
19399380 5468
38798760 7655
58198140 9113
77597520 9842
116396280 12758'''

'''
0
2 2
4 3
1
6 5
12 8
24 11
2
30 14
60 23
120 32
180 38
3
210 41
420 68
840 95
1260 113
1680 122
4
4620 203
9240 284
13860 338
18480 365
27720 473
5
60060 608
120120 851
180180 1013
240240 1094
360360 1418
6
1021020 1823
2042040 2552
3063060 3038
4084080 3281
6126120 4253
7
19399380 5468
38798760 7655
58198140 9113
77597520 9842
116396280 12758
8
446185740 16403
892371480 22964
1338557220 27338
1784742960 29525
2677114440 38273
5354228880 49208
9
25878772920 68891
38818159380 82013
51757545840 88574
77636318760 114818
155272637520 147623
10
802241960520 206672
1203362940780 246038
1604483921040 265721
2406725881560 344453
4813451763120 442868
7220177644680 482234
11
29682952539240 620015
44524428808860 738113
59365905078480 797162
89048857617720 1033358
178097715235440 1328603
267146572853160 1446701
12
1217001054108840 1860044
1825501581163260 2214338
2434002108217680 2391485
3651003162326520 3100073
7302006324653040 3985808
10953009486979560 4340102'''
