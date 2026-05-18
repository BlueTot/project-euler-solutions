fib = [0, 1]
total=0
while fib[-1] < 4000000:
    fib.append(num:=fib[-2]+fib[-1])
    total += num if num % 2 == 0 else 0
print(total)