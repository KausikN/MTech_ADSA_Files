'''
DFS Algorithm
'''

# Imports
import json
import numpy as np
from copy import deepcopy

# Main Vars
I = np.inf
time = 0

# Utils Functions
def FixAdjMatrix(AdjMatrix):
    '''
    Fix the AdjMatrix
    '''
    AdjMatrix = np.array(AdjMatrix)
    for i in range(AdjMatrix.shape[0]):
        for j in range(AdjMatrix.shape[1]):
            if i != j:
                if AdjMatrix[i][j] == 0:
                    AdjMatrix[i][j] = I
    return AdjMatrix

# Main Functions
def DFS(AdjMatrix, source=0):
    '''
    Perform DFS on the given Graph starting at the source
    '''
    global time

    # Initialize
    AdjMatrix = np.array(AdjMatrix)
    N = AdjMatrix.shape[0]
    visited = np.zeros(N, dtype=bool)
    parent = np.ones(N, dtype=int) * -1
    d = np.ones(N, dtype=int) * -1
    f = np.ones(N, dtype=int) * -1

    Results = {}

    time = 0
    # DFS
    def DFS_rec(u):
        '''
        Recursive DFS
        '''
        global time

        visited[u] = True
        print("VISITED", u)
        time += 1
        d[u] = time
        for v in range(N):
            if not (AdjMatrix[u, v] == I) and not visited[v]:
                parent[v] = u
                DFS_rec(v)
        time += 1
        f[u] = time
    
    DFS_rec(source)

    Results['d'] = d.tolist()
    Results['f'] = f.tolist()
    Results['parent'] = parent.tolist()

    # Return
    return Results

# Driver Code
# Params
AdjMatrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

Source = 0
# Params

# RunCode
AdjMatrix = FixAdjMatrix(AdjMatrix)
Results = DFS(AdjMatrix, Source)
jsonData = json.dumps(Results, indent=4)
print(jsonData)