# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.



import sys

def sumto(n): return (n + n**2) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    

    n_3 = n // 3
    n_5 = n // 5
    n_15 = n // 15

    result = sumto(n_3) * 3 + sumto(n_5) * 5 - sumto(n_15) * 15
    print(int(result))