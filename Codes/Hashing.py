'''
Hashing Codes
'''

# Imports
import sympy

# Main Functions
# Prime Functions
def ClosestPrime(n):
    '''
    Closest Prime to n greater than n
    '''
    if n <= 2:
        return 2
    i = n
    while True:
        if sympy.isprime(i):
            return i
        i += 1

def ClosestPowerOf2(n):
    '''
    Closest Power of 2 to n
    '''
    if n == 0:
        return 0
    binL = len(str(int(abs(n), 2)))
    lP = 2 ** binL
    rP = 2 ** (binL + 1)
    if abs(n) - lP <= rP - abs(n):
        return lP
    return rP

# Hash Functions
# Division Method
def Hash_DivisionMethod(k, m):
    '''
    Division Method
    '''
    return k % m

def Hash_MultiplicationMethod(k, m, A):
    '''
    Multiplication Method
    '''
    kA = k * A
    kA_frac = kA - int(kA)
    hk = int(kA_frac * m)
    return hk

def Hash_UniversalMethod(k, a, b, p, m):
    '''
    Universal Method
    '''
    hk = (((a * k) + b) % p) % m
    return hk

# Probe Functions
def Probe_Linear(hk, i, m):
    '''
    Linear Probe
    '''
    return (hk + i) % m

def Probe_Quadratic(hk, i, c1, c2, m):
    '''
    Quadratic Probe
    '''
    return (hk + c1 * i + c2 * (i**2)) % m

def DoubleHashing(hk1, hk2, i):
    '''
    Double Hashing
    '''
    return (hk1 + i * hk2) % m

# Driver Code
# Params
n = 10000
m = 100

# Mul Hash
A = ((5**(0.5)) - 1) / 2

# Univ Hash
p = ClosestPrime(n)

k = 23
# Params

# RunCode
closest_prime = ClosestPrime(int(n/3))
print("Closest Prime to n greater than n:", closest_prime)
closest_pw2 = ClosestPowerOf2(closest_prime)
print("Closest Power of 2 to closest prime:", closest_pw2)
print("Diff:", abs(closest_prime-closest_pw2))