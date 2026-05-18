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

ps = primes(10**9)

size = 3
lst = {}
row, col = 0, 0
lst[(row, col)] = 1
layer = 0
count = 1
numprimes = 0

while True:

    if row == col:

        col += 1
        layer += 1
        if layer > size:
            numdiagonals = 4*size+1
            ratio = numprimes / numdiagonals
            print(size, numprimes, numdiagonals, ratio)
            if ratio < 0.1:
                print(size)
                print(2*size+1)
                break
            size += 1
        count += 1
        if abs(row) == abs(col):
            if count in ps:
                numprimes += 1
        
    else:

        while row > -layer:
            row -= 1
            count += 1
            if abs(row) == abs(col):
                if count in ps:
                    numprimes += 1
            
        while col > -layer:
            col -= 1
            count += 1
            if abs(row) == abs(col):
                if count in ps:
                    numprimes += 1
            
        while row < layer:
            row += 1
            count += 1
            if abs(row) == abs(col):
                if count in ps:
                    numprimes += 1
            
        while col < layer:
            col += 1
            count += 1
            if abs(row) == abs(col):
                if count in ps:
                    numprimes += 1

# seq1 = lambda x: 4*x**2 - 8*x + 5
# seq2 = lambda x: 4*x**2 - 10*x+ 7
# seq3 = lambda x:4*x**2 - 6*x + 3

# size = 0
# numprimes = 0
# while True:
#     num_diagonals = 4*size + 1
#     # print([seq1(size), seq2(size), seq3(size)])
#     for n in [seq1(size-1), seq2(size-1), seq3(size-1)]:
#         print(n)
#         if n in ps:
#             numprimes += 1
#     ratio = numprimes/num_diagonals
#     if ratio < 0.1:
#         print(2*size+1)
#         break
#     size += 1


