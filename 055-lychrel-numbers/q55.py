def reverse(num):
    lst = [i for i in str(num)]
    lst.reverse()
    return int("".join(lst))

def is_palindrome(n):
    front, rear = 0, len(n)-1
    while True:
        if n[front] != n[rear]:
            return False
        if front == rear or abs(front - rear) == 1:
            return True
        front += 1
        rear -= 1

lychrel = 0
for n in range(1, 10000):
    curr = n
    for numiterations in range(50):
        curr += reverse(curr)
        if is_palindrome(str(curr)):
            break
    if not (numiterations < 49):
        lychrel += 1
print(lychrel)

