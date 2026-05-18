longest = 0
n = None
for num in range(1, 10**6):
    curr = num
    length=0
    while curr != 1:
        if curr % 2 == 0:
            curr /= 2
        else:
            curr = 3*curr+1
        length+=1
    if length > longest:
        longest = length
        n = num
    print(num)
print(longest)
print(n)