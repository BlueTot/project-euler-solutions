from math import sqrt

def is_pandigital(num):
    return set(str(num)) == set("123456789")

def pow(n, x): # power function
    product = 1
    for _ in range(x):
         product *= n
         if product > 10**30:
             product /= 10**10 # divide to only keep the head
    return product

phi = (1+sqrt(5))/2 # golden ratio

def fib(n): # binet's formula for fibonacci numbers
    return int((pow(phi,n) - pow(1-phi,n))/sqrt(5))

fibs = [1, 1]
while True:
    fibs.append((fibs[-1] + fibs[-2]) % 10**9) # calculate tail of next fib (mod to keep tail)
    if is_pandigital(fibs[-1]): # check tail is pandigital
        n = len(fibs)
        num = fib(n) # calculate number
        print(n, is_pandigital(str(num)[:9]))
        if is_pandigital(str(num)[:9]): # check head is pandigital
            break