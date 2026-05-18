from math import factorial

def eval(nth_term, n): # evaluate polynomial function at n
    total = 0
    for coefficient, degree in nth_term:
        total += coefficient * (n ** degree)
    return total

def final_diff(sequence): # function to get first final difference in the sequence (equal to n!*a where n = degree)
    if len(sequence) == 1: # base case
        return sequence[0]
    else:
        differences = []
        for idx in range(1, len(sequence)):
            differences.append(sequence[idx]-sequence[idx-1]) # calculate differences
        return final_diff(differences)

def nth_term_sequence(sequence): # Recursive function to find nth term polynomial
    degree = len(sequence) - 1 # calculate degree of polynomial resulting from sequence
    if degree == 0: return [(sequence[0], 0)] # base case
    coefficient = final_diff(sequence) / factorial(degree) # get coefficient = final diff / degree!
    reduced_sequence = [num - eval([(coefficient, degree)], n+1) for n, num in enumerate(sequence[:-1])] # reduce by new term of polynomial
    return [(coefficient, degree)] + nth_term_sequence(reduced_sequence) # recursion on reduced sequence

def generating_function(n): return (1+n**11) / (1+n)

def euler101():

    total = 0
    for k in range(1, 11):
        func = nth_term_sequence(seq := [generating_function(i) for i in range(1, k+1)])
        n = 1
        while True:
            num = eval(func, n)
            if num != generating_function(n):
                total += num
                break
            n += 1

    return total

if __name__ in "__main__":
    print(euler101())