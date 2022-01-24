'''
Birthday Problem
'''

# Imports
import functools
import math
import numpy as np
from tqdm import tqdm

# Main Functions
def CalcBirthdayMatchProb(n):
    '''
    Calculates the probability of a match between two people
    '''
    # Calculate the probability of a match
    maxDays = 365
    a = 1.0
    for i in tqdm(range(maxDays-n+1, maxDays)):
        a = a * (i/maxDays)
    prob = 1 - a
    return prob

def QuadraticSolver(a, b, c):
    '''
    Solves the quadratic equation
    '''
    # Calculate the discriminant
    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    # Calculate the roots
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    return root1, root2

# Driver Code
# Params
n = 50
# Params

# RunCode
p = CalcBirthdayMatchProb(n)
print(p)

print((1/8)*(1/7)*(1/6))