total = 0
curr = 2
while len(str(curr)) < 7:
    digits = [int(digit) for digit in str(curr)]
    if sum([digit**5 for digit in digits]) == curr:
        print(curr)
        total += curr
    curr += 1
print(total)