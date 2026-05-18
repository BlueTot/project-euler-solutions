def is_palindrome(n):
    front, rear = 0, len(n)-1
    while True:
        if n[front] != n[rear]:
            return False
        if front == rear or abs(front - rear) == 1:
            return True
        front += 1
        rear -= 1

s = 0
palindromes = set()
for start in range(1, 10000):
    print(start)
    total = start**2
    for end in range(start+1, 10000):
        total += end**2
        if is_palindrome(str(total)) and total < 10**8:
            palindromes.add(total)
            # print(total)
print(sum(palindromes))

# total = 0
# for a in range(1, 10000):
#     print(a)
#     for b in range(a+1, 10000):
#         num = b*(b+1)*(2*b+1)//6 - a*(a-1)*(2*a-1)//6
#         if is_palindrome(str(num)) and num < 10**8:
#             total += num
#             # print(num)
# print(total)