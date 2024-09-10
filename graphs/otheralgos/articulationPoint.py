# To find the articulation points in the graph
from collections import deque
import heapq

def articulationPoints(n, edges):
    adj = [[] for i in range(n)]

    for edge in edges:
        u_, v_ = edge
        adj[u_].append(v_)
        adj[v_].append(u_)
    
    # Adjacency list is prepared
    firstContact = dict(); time = 1
    visited = {i:0 for i in range(n)}

    def dfs(node, parent, fT):
        actualtime = firstContact[node] = fT
        visited[node] = 1
        adjnodes = adj[node]
        for nextnode in adjnodes:
            if nextnode == parent:
                continue
            elif visited[nextnode] == 1:
                actualdist = min(actualdist, firstContact[nextnode])
                #Edge is not a critical one
            else:
                time += 1
                actual = dfs(nextnode, node, time)
                if actual > fT:
                    criticalNodes.add(node)
                else:
                    actualdist = min(actual, actualdist)
        return actualdist
    
    dfs(0, None, time)

    if len(adj[0]) == 1 and 0 in criticalNodes:
        criticalNodes.remove(0)
    
    return criticalNodes


