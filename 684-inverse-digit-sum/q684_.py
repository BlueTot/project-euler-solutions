M = 1000000007
# sum = 0


# sum += 45

# for i in range(1,3):
#     for j in range(1,10):
#         sum += j*(10**i)+9


# print(sum)

curr = 1
for _ in range(200):
    curr = (curr * 49) % M
    print(curr, _)