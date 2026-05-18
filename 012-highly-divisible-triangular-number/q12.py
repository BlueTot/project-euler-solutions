factors = 1
triangulars = [1]

def factors_of(num):
    factors = []
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0:
            factors.append(factor)
            if factor != num / factor:
                factors.append(num//factor)
    return len(factors)

while True:
    num_of_factors = factors_of(triangulars[-1])
    if num_of_factors >= 500:
        print(num_of_factors, triangulars[-1])
        break
    print(len(triangulars))
    triangulars.append(triangulars[-1]+len(triangulars)+1)
    