def square_of_digits(num):
    return sum([int(digit)**2 for digit in str(num)])

endsin89 = set()
endsin1 = set()
for num in range(2, 10**7):
    print(num)
    curr = num
    stack = set()
    stack.add(curr)
    while True:
        curr = square_of_digits(curr)
        stack.add(curr)
        if curr in endsin89 or 89 in stack:
            endsin89.add(num)
            break
        if curr in endsin1 or 1 in stack:
            endsin1.add(num)
            break
print(len(endsin89))
