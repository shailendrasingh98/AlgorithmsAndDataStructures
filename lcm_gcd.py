#!/bin/python3

import os
import sys

# GCD and LCM are not in math module.  They are in gmpy, but these are simple enough:
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def Lcm(a):
    x = a[0]
    for i in a:
       x = lcm(x, i)
    return x

def Gcd(b):
    x = b[0]
    for i in b:
       x = gcd(x, i)
    return x


def getTotalX(a, b):
    count = 0
    l = Lcm(a)
    g = Gcd(b)
    for i in range(1,int(g/l)+1):
        if(sum((i*l)%n for n in a)+sum(n%(i*l) for n in b))==0:
            count+=1
    return count

def isPrime(n):

    if n <=1:return False
    if n<=3: return False
    if n%2 ==0 or n%3 == 0: return False
    #if n is divisible by 6k+1 where k >=5
    #prime no greater than 3 will be form of 6k+1
    #not must, check 6k+1 are factors of n
    for i in range(5, n+1, 6):
        if i*i <=n:
            if n%i==0 or n%(i+2) ==0:
                return False
    return True

def primes_sieve2(limit):
    a = [True] * limit           # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i): # Mark factors non-prime
                a[n] = False

def abModm(a, b, m):
    a = a%m
    b = b%m
    res =0
    while (b>0):
        if (b&1):res = (res+a)%m
        a = (a<<1)%m
        b = (b>>1)%m
    return res

def expo(a, b, m):
    res = 1
    while(b&1):
        res = abModm(res, a, m)
        b>>=1
        a = abModm(a,a,m)

def kthDigit(a,b,k):
    m = 10**k
    res = 1
    for i in range(b):
        res = abModm(res, a, m)
    print('res', res)
    m//=10
    return res//m

def num_factors(n):
    results = set()
    sqr = int(n**0.5)
    step = 2 if n%2 else 1
    for i in range(1, sqr+1, step):
        if n % i != 0: continue
        results.update([i, n//i])
    return results

if __name__ == '__main__':
    #OUTPUT_PATH =
    #f = open(os.environ['ONEDRIVECONSUMER'], 'w')

    #nm = input().split()

    #n = int(nm[0])

    #m = int(nm[1])

    #a = list(map(int, input().rstrip().split()))

    #b = list(map(int, input().rstrip().split()))
    a = [2, 4]
    b = [16, 32, 96]
    total = getTotalX(a, b)
    print(total)
    print('Yes') if isPrime(97) else print('No')
    print(kthDigit(5,5,2))
    print([p for p in primes_sieve2(100)])
    #f.write(str(total) + '\n')

    #f.close()
