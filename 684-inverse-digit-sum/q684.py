M = 1000000007

exps = [1]
for _ in range(10**7):
    if (exps[-1]*10) % M == 49:
        print("found", _, (exps[-1]*10) % M)
    #print((exps[-1]*10) % M, _+1)
    exps.append((exps[-1]*10) % M)


print("E")
def exp(power):
    # base = power // 18
    # if base > 0:
    #     pbase = (49 ** base) % M
    # else:
    #     pbase = 1
    # for _ in range(power % 18):
    #     pass

    return exps[power]

# def exp(power):
#     return (10 ** power) % M

def s(n):
    start = n % 9
    power = n // 9
    return ((start * exp(power)) % M + (((exp(power) - 1) % M) if power > 0 else 0)) % M

def S(k):
    num_batches = k // 9
    if num_batches > 1:
        return ((45 + 60 * (exp(num_batches - 1) - 1) - 9 * (num_batches - 1)) % M + sum([s(k) % M for k in range(num_batches*9+1, k+1)]) % M) % M
    return sum([s(k) % M for k in range(1, k+1)]) % M

# print(S(9))
# print(S(18))
# print(S(27))
# print(S(37))

# print(s(10))
# print(S(20))

fibs = [0, 1]
while len(fibs) < 90+1:
    fibs.append(fibs[-1]+fibs[-2])

total = 0
for i in range(2, 90+1):
    print(i, fibs[i])
    total += (val := S(fibs[i]) % M)
    print(val)
total %= M
print(total)

# '''(a*b)%c = (a%c*b%c)%c'''

# '''
# E
# 2 1
# 1
# 3 2
# 3
# 4 3
# 6
# 5 5
# 15
# 6 8
# 36
# 7 13
# 46
# 8 21
# 123
# 9 34
# 4060
# 10 55
# 799939
# 11 89
# 999999877
# 12 144
# 957999857
# 13 233
# 449999747
# 14 377
# 200499610
# 15 610
# 234736622
# 16 987
# 762473448
# 17 1597
# 245476531
# 18 2584
# 17182237
# 19 4181
# 507753717
# 20 6765
# 833762564
# 21 10946
# 71275037
# 22 17711
# 169809855
# 23 28657
# 865054141
# 24 46368
# 730754896
# 25 75025
# 321484685
# 26 121393
# 980987924
# 27 196418
# 947427333
# 28 317811
# 512629410
# 29 514229
# 316911850
# 30 832040
# 586932692
# 31 1346269
# 580788685
# 32 2178309
# 772719212
# 33 3524578
# 556133873
# 34 5702887
# 891129868
# 35 9227465
# 928073644
# 36 14930352
# 939487841
# 37 24157817
# 704094239
# 38 39088169
# 238707197
# 39 63245986
# 390105610
# 40 102334155
# 600730853
# 41 165580141
# 346471432
# 42 267914296
# 20956330
# 43 433494437
# 652736415
# 44 701408733
# 467472521
# 45 1134903170
# 252528737
# 46 1836311903
# 639512242
# 47 2971215073
# 978994352
# 48 4807526976
# 168874830
# 49 7778742049
# 226398574
# 50 12586269025
# Traceback (most recent call last):
#   File "c:\Users\nhlo\Desktop\Personal\school_coding\Year12\project_euler\q684.py", line 37, in <module>
#     total += (val := S(fibs[i]) % M)
#                      ^^^^^^^^^^
#   File "c:\Users\nhlo\Desktop\Personal\school_coding\Year12\project_euler\q684.py", line 19, in S
#     return ((45 + 60 * (exp(num_batches - 1) - 1) - 9 * (num_batches - 1)) % M + sum([s(k) % M for k in range(num_batches*9+1, k+1)]) % M) % M
#                         ^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\nhlo\Desktop\Personal\school_coding\Year12\project_euler\q684.py", line 9, in exp
#     return exps[power]
#            ~~~~^^^^^^^
# IndexError: list index out of range'''
