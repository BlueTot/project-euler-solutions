#!/bin/python3


# we are given a+b+c = N, so c = N-b-a
# we must have c**2 = a**2 + b**2
# substituting c and rearranging, we get
# b = (N**2 - 2Na)/(2N-2a)

# provides us with a linear time algorithm
# by iterating through all values of a

def euler9(N: int) -> int:

    res = -1

    for a in range(3, N):
        q, r = N*N - 2*N*a, 2*N - 2*a
        if (q % r != 0):
            continue
        b = q // r
        if (b > 0 and N-b-a > 0):
            abc = a * b * (N-b-a)
            res = max(res, abc)

    return res


n = int(input())
for _ in range(n):
    print(euler9(int(input())))


