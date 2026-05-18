def is_palindrome(n):
    front, rear = 0, len(n)-1
    while True:
        if n[front] != n[rear]:
            return False
        if front == rear or abs(front - rear) == 1:
            return True
        front += 1
        rear -= 1

def main():
    largest = 1
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            p = num1 * num2
            if is_palindrome(str(p)) and p > largest:
                largest = p
                print(p)
    print(largest)
            
main()