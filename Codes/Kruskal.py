'''
Kruskals Algorithm
'''

# Imports
import json
import numpy as np
from copy import deepcopy

# Main Vars
I = np.inf

# Utils Functions
def FixAdjMatrix(AdjMatrix):
    '''
    Fix the AdjMatrix
    '''
    AdjMatrix = np.array(AdjMatrix, dtype=float)
    for i in range(AdjMatrix.shape[0]):
        for j in range(AdjMatrix.shape[1]):
            if i != j:
                if AdjMatrix[i, j] == 0:
                    AdjMatrix[i, j] = I
    return AdjMatrix

# Main Functions
def Kruskal(AdjMatrix):
    '''
    Perform Kruskals Algorithm on the given Graph
    '''
    # Initialize
    AdjMatrix = np.array(AdjMatrix)
    N = AdjMatrix.shape[0]

    # Initialize
    MST = []
    Edges = []
    for i in range(N):
        for j in range(i+1, N):
            if AdjMatrix[i][j] != I:
                Edges.append((i, j, AdjMatrix[i][j]))
    
    # Sort Edges
    Edges.sort(key=lambda x: x[2])

    # Initialize
    Parent = [i for i in range(N)]
    Rank = [0 for i in range(N)]

    def Find(Parent, i):
        '''
        Find the Parent of the given Node
        '''
        if Parent[i] == i:
            return i
        else:
            return Find(Parent, Parent[i])

    def Union(x, y):
        '''
        Union the given Nodes
        '''
        xroot = Find(Parent, x)
        yroot = Find(Parent, y)
        if Rank[xroot] < Rank[yroot]:
            Parent[xroot] = yroot
        elif Rank[xroot] > Rank[yroot]:
            Parent[yroot] = xroot
        else:
            Parent[yroot] = xroot
            Rank[xroot] += 1

    # Perform Kruskals Algorithm
    for i in range(len(Edges)):
        u, v, w = Edges[i]
        if Find(Parent, u) != Find(Parent, v):
            MST.append((u, v, w))
            Union(u, v)
    
    # Return
    return MST

# Driver Code
# Params
AdjMatrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
# Params

# RunCode
AdjMatrix = FixAdjMatrix(AdjMatrix)
MST = Kruskal(AdjMatrix)
jsonData = json.dumps(MST, indent=4)
print(jsonData)