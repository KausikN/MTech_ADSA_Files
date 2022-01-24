'''
Prims Algorithm
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
def Prim(AdjMatrix, source=0):
    '''
    Perform Prims Algorithm on the given Graph
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

    # Initialize
    Parent = [i for i in range(N)]
    Rank = [I for i in range(N)]
    Rank[source] = 0
    Q = list(range(N))

    # Loop
    while len(Q) > 0:
        # Find the minimum edge
        min_edge = I
        u = -1
        v = -1
        for i in Q:
            for j in Q:
                if i != j:
                    if AdjMatrix[i][j] != I and AdjMatrix[i][j] < min_edge:
                        min_edge = AdjMatrix[i][j]
                        u = i
                        v = j

        # Add the edge to the MST
        MST.append((u, v, min_edge))

        # Update the AdjMatrix
        AdjMatrix[u][v] = I
        AdjMatrix[v][u] = I

        # Update the Q
        Q.remove(u)
        Q.remove(v)

        # Update the Rank
        if Rank[u] > Rank[v]:
            Parent[u] = v
            Rank[u] = Rank[v]
        else:
            Parent[v] = u
            Rank[v] = Rank[u]

# Driver Code
# Params
AdjMatrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])
# Params

# RunCode
AdjMatrix = FixAdjMatrix(AdjMatrix)
MST = Prim(AdjMatrix)
jsonData = json.dumps(MST, indent=4)
print(jsonData)