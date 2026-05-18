import sys

sys.setrecursionlimit(10**7)
sys.set_int_max_str_digits(10**6)


factorials = [1,1]

for i in range(2,2023):
	factorials.append(i*factorials[i-1])

d = [0]

def choose(n,r):
	return((factorials[n])//((factorials[r])*(factorials[n-r])))

def pow(n, x):
    product = 1
    for _ in range(x):
        product = (product * n % base)
    return product


d = [0,9]

base = 1000000007
N = 2022

for i in range(2,N+1):
	n = i
	max_r = (n-1)//2
	total = 0
	for j in range(max_r+1):
		#total += choose(n,j)*pow(9, j+1)
		total += choose(n,j)*(9**(j+1))
	d.append((d[i-1]+total)%base)
	print(i)

print(d[N]%base)

#n = 10
#21893256
#21893256

#n=20
#136903862
#136903862

#n=50
#568763107
#568763107

#n=100
#422210470
#422210470

#n=200
#623973713
#623973713

#n=300
#509164210
#509164210

#n=600
#762602684
#762602684

#n=1000
#279925126
#279925126
