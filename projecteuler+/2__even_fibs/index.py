#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    first = 1
    second = 2

    even_sum = 0

    while second < n:
        if second % 2 == 0:
            even_sum += second
        temp = second
        second = first + second
        first = temp

    print(even_sum)