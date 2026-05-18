def is_palindrome(n):
    front, rear = 0, len(n)-1
    while True:
        if n[front] != n[rear]:
            return False
        if front == rear or abs(front - rear) == 1:
            return True
        front += 1
        rear -= 1

total = 0
for num in range(1, 10**6):
    if is_palindrome(str(num)) and is_palindrome(str(bin(num))[2:]):
        total += num
        print(num)
print(total)