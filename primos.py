import math
import sys

def is_prime(n):
    isPrime = 1 != n
    for i in range(2, n//2 + 1):
        if (n % i == 0):
            isPrime = False
            break
            
    return isPrime