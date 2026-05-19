#!/bin/python3


def collatz_next(n: int):
    return n//2 if n % 2 == 0 else 3*n+1


# precompute the length for all values from 1 to MAX_N = 5 * 10^6
# if i is even, we have precomputed i / 2 because we go from 1 to MAX_N
# if i is odd, then we make a stack and keep pushing to it until we find a value
# that we've seen before
# then we fill in the length on the way back

# we avoid storing length entries for values > MAX_N
# to prevent memory error


MAX_N = 5*10**6
length = [-1]*(MAX_N+1)
length[1] = 1

for i in range(2, MAX_N+1):

    if length[i] != -1:
        continue

    if i % 2 == 0:
        length[i] = 1 + length[i//2]

    else:

        stack = []
        curr = i

        # push to the stack until we find a value we know
        while curr > MAX_N or length[curr] == -1:
            stack.append(curr)
            curr = collatz_next(curr)

        l = length[curr]

        # pop and fill in values
        while stack:
            curr = stack.pop()
            l += 1
            if curr <= MAX_N:
                length[curr] = l


# precompute prefix maximums so each test case
# just needs to return the value

res = [-1]*(MAX_N+1)
best_i, max_length = -1, 0 

for i in range(2, MAX_N+1):
    if length[i] >= max_length:
        max_length = length[i]
        best_i = i
    res[i] = best_i


def euler14(N: int) -> int:
    return res[N]


n = int(input())
for _ in range(n):
    print(euler14(int(input())))
