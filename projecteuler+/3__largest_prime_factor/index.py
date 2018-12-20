#!/bin/python3

import sys

import math

def prime_factors(n):
    prime_factors = [1]
    
    while n % 2 == 0:
        prime_factors.append(2)

        n = int(n / 2)
    
    i = 3
    while i < math.sqrt(n) + 1:
        while n % i == 0:
            prime_factors.append(i)

            n = int(n / i)

        i += 2 



    if n > 2:
 
        prime_factors.append(n)


    return prime_factors

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    primes = prime_factors(n)
    print(primes[len(primes) - 1])