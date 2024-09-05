# TO find the edges that break the graph to 2 if removed

# These are the edges that are not present in a loop

#Procedure:
# Run dfs in a graph, if there is a loop add all the nodes to that dfs.
# The nodes in the loop start fromm the node that triggered the visited to itself in a iteration.
# All the remaining nodes are those that are not in the loop

from collections import deque

def criticalConnection(n, edges):
    adj = [float('inf') for i in range(n)]
    

n = 6
edges = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]

res = criticalConnection(n, edges)

print(res)