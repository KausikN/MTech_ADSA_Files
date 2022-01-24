'''
BFS Algorithm
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
    AdjMatrix = np.array(AdjMatrix)
    for i in range(AdjMatrix.shape[0]):
        for j in range(AdjMatrix.shape[1]):
            if i != j:
                if AdjMatrix[i][j] == 0:
                    AdjMatrix[i][j] = I
    return AdjMatrix

# Main Functions
def BFS(AdjMatrix, source=0):
    '''
    Perform BFS on the given Graph starting at the source
    '''

    # Initialize
    AdjMatrix = np.array(AdjMatrix)
    N = AdjMatrix.shape[0]
    visited = np.zeros(N, dtype=float)

    Results = {}
    trace = []
    
    currIter = {'iter': 0, 'visited': deepcopy(visited.tolist())}
    trace.append(currIter)

    visited[source] = 1.0

    currIter = {'iter': 0, 'visited': deepcopy(visited.tolist())}
    trace.append(currIter)

    # BFS
    queue = [source]
    while len(queue) > 0:
        # Pop
        u = queue.pop(0)
        # Update
        visited[u] = 1.0
        print("VISITED", u)
        # Push
        for v in range(AdjMatrix.shape[1]):
            if not (AdjMatrix[u, v] == I) and not (visited[v] == 1.0):
                queue.append(v)
                visited[v] = 0.5
        # Update Trace
        currIter = {'iter': len(trace), 'visited': deepcopy(visited.tolist())}
        trace.append(currIter)
    
    Results = {}
    Results['source'] = source
    Results['visited'] = visited.tolist()
    Results['trace'] = trace
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
Results = BFS(AdjMatrix, Source)
jsonData = json.dumps(Results, indent=4)
print(jsonData)