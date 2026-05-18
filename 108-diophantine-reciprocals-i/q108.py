ln, ll = 0, 0
for n in range(10, 10**6, 10):
    sols = set()
    for x in range(n+1, 2*n+1):
        if n*x % (x-n) == 0:
            y = int(n*x/(x-n))
            sols.add((min(x, y), max(y, y)))
    if len(sols) > 1000:
        print(n, len(sols))
        break
    if len(sols) > ll:
        ll = len(sols)
        ln = n
        print(ln, ll)

'''
10 5
20 8
30 14
60 23
120 32
180 38
210 41
360 53
420 68
840 95
1260 113
1680 122
2520 158
4620 203
7560 221
9240 284
13860 338
18480 365
27720 473
55440 608
83160 662
110880 743
120120 851
180180 1013'''