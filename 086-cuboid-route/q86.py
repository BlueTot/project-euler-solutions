# from math import sqrt

# def pyths(N) : 
#     a, b, c, m = 0, 0, 0, 2
#     while a < N and b < N and c < N : 
#         for n in range(1, m) : 
#             a = m**2  - n**2
#             b = 2*m*n
#             c = m**2 + n**2
#             if c > N : 
#                 break
#             yield a, b, c
#         m  += 1

# def pyths3(N):

#     pyths = set()
#     a, m = 0, 2
#     while a < N: 
#         for n in range(1, m): 
#             a = m**2  - n**2
#             b = 2*m*n
#             c = m**2 + n**2
#             if a > N : 
#                 break
#             pyths.add((a, b, c))
#         m  += 1

#     pyths2 = set()
#     for a, b, c in pyths:
#         for k in range(1, N//max(a, b, c)+1):
#             pyths2.add((a*k, b*k, c*k))
    
#     return pyths2

# N = 100
# cuboids = {}
# for a, b, c in pyths3(N):
#     for x in range(1, a):
#         dims = tuple(sorted((b, x, a-x)))
#         if dims not in cuboids:
#             cuboids[dims] = [c]
#         else:
#             cuboids[dims].append(c)
#     for x in range(1, b):
#         dims = tuple(sorted((a, x, b-x)))
#         if dims not in cuboids:
#             cuboids[dims] = [c]
#         else:
#             cuboids[dims].append(c)
    
# print(len(cuboids))
# print(sorted(list(cuboids.keys())))

# M = 100
# integer_length = set()
# for l in range(1, M+1):
#     for w in range(1, M+1):
#         for h in range(1, M+1):
#             x1 = sqrt(l**2 + (w+h)**2)
#             x2 = sqrt((l+h)**2 + w**2)
#             x3 = sqrt((l+w)**2 + h**2)
#             shortest_path = min(x1, x2, x3)
#             if shortest_path % 1 == 0:
#                 integer_length.add(tuple(sorted((l, w, h))))
# print(sorted(list(integer_length)))
# print(len(integer_length))

# def proper_divisors(num):
#     for factor in range(1, int(num ** 0.5)+1):
#         if num % factor == 0 and factor != num:
#             yield num // factor, factor

# for n in [4]:
#     for m, n in proper_divisors(n//2):
#         a = m**2 - n**2
#         for x in range(1, a):
#             print(sorted((n, a, a-x)))