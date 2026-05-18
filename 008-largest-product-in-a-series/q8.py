#!/bin/python3

def euler8(N: int, K: int, number: str) -> int:

    res = 0
    product = 1
    i = 0
    window = 0

    # sliding window of size K over the number string

    while i < N:

        # if we see a 0, skip past it and reset window to size 0
        if number[i] == "0":
            window = 0
            product = 1

        # while window not full, keep adding
        elif window < K:
            product = product * int(number[i])
            window += 1

        # once window is full, move it along
        else:
            product = product * int(number[i]) // int(number[i-K])

        # if window is full, record the maximum
        if window == K:
            res = max(res, product)

        i += 1

    return res

n = int(input())
for _ in range(n):
    N, K = list(map(int, input().split()))
    number = input()
    print(euler8(N, K, number))

