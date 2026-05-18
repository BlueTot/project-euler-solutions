from math import factorial

def digit_factorials(num):
    return sum([factorial(int(i)) for i in str(num)])

lengths = {}
total = 0
for num in range(2, 10**6):
    length = 1
    curr = num
    stack = set()
    while True:
        curr = digit_factorials(curr)
        if curr in stack:
            break
        stack.add(curr)
        length += 1
    lengths[num] = length
    if length == 60:
        total += 1
    print(num)
print(total)