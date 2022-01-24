'''
Compare Time Complexity Functions to determine point of crossing
'''

# Imports
import functools
import math
import numpy as np
import matplotlib.pyplot as plt

# Main Functions
def CompareTimeFuncs(f1, f2, checkRange=[0, 100]):
    # Init Range
    x = range(checkRange[0], checkRange[1])

    y1 = []
    y2 = []
    crossPoints = []

    greaterFunc = 1 if f1(checkRange[0]) > f2(checkRange[0]) else 2
    for i in x:
        y1.append(f1(i))
        y2.append(f2(i))
        if y1[-1] > y2[-1] and greaterFunc == 2:
            greaterFunc = 1
            crossPoints.append([i, 1])
        elif y1[-1] < y2[-1] and greaterFunc == 1:
            greaterFunc = 2
            crossPoints.append([i, 2])

    # Plot Graphs
    plt.plot(x, y1, label='f1(x)')
    plt.plot(x, y2, label='f2(x)')
    for cP in crossPoints:
        plt.axvline(cP[0], color='r', linestyle='--')
    plt.legend()
    plt.show()

    return crossPoints

# Driver Code
# Params
def logstar(x=",", y=""):
    i = 1
    while(x > 1):
        x = math.log2(x)
        i += 1
    return i

def f1(x, 
y):
    y = math.log2(logstar(x))
    return y

def f2(x):
    y = logstar(math.log2(x))
    return y

# Params
Func_1 = f1
Func_2 = f2
checkRange = [1, 100]
# Params

# RunCode
crossPoints = CompareTimeFuncs(Func_1, Func_2, checkRange)
print(crossPoints)