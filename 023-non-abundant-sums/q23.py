def proper_divisors(num):
    factors = []
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0 and factor != num:
            factors.append(factor)
            if factor != num / factor and num//factor != num:
                factors.append(num//factor)
    return factors

abundants = set()
for num in range(1, 28123):
    if sum(proper_divisors(num)) > num:
        abundants.add(num)
print(abundants)

# nums = set()
# for num1 in abundants:
#     for num2 in abundants:
#         nums.add(num1+num2)
# print(nums)

# total = 0
# for num in range(1, 28123+1):
#     if num not in nums:
#         total += num
# print(total)