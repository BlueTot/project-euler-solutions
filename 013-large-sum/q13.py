#!/bin/python3


def euler13(nums: list[int]) -> str:
    total = sum(nums)
    return str(total)[:10]


n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

print(euler13(nums))

