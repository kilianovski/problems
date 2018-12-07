# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def prime_factors(n):
    prime_factors = [1]
    
    while n % 2 == 0:
        prime_factors.append(2)
        print(2)
        n = int(n / 2)
    
    i = 3
    while i < math.sqrt(n) + 1:
        while n % i == 0:
            prime_factors.append(i)
            print(i)
            n = int(n / i)

        i += 2 



    if n > 2:
        print(n)
        prime_factors.append(n)


    print('END!')
    return prime_factors


n = 10
# res = prime_factors(n)
# print(res)
from functools import reduce
# 

prime_factors(9)
for i in range(1, 99999):
    print(i)
    res = prime_factors(i)
    product = reduce(lambda a, b: a*b, res, 1)
    if product != i:
        print(res)
        print(product)
        print('-----')
    
