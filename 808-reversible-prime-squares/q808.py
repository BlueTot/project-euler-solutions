from math import sqrt

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = set()
    list_of_primes.add(2)

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.add(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

def is_palindrome(n):
    front, rear = 0, len(n)-1
    while True:
        if n[front] != n[rear]:
            return False
        if front == rear or abs(front - rear) == 1:
            return True
        front += 1
        rear -= 1

ps1 = primes(5*10**7)
ps2 = sorted(list(primes(5*10**7)))

sqs = []
for p in ps2:
    sq = p ** 2
    if not is_palindrome(str(sq)):
        lst = [i for i in str(sq)]
        lst.reverse()
        reverse = int("".join(lst))
        if sqrt(reverse) % 1 == 0:
            if int(sqrt(reverse)) in ps1:
                print(sq)
                sqs.append(sq)
    if len(sqs) == 50:
        print("done")
        print(sum(sqs))
        break

