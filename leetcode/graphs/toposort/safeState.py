# To find all the safe states in a state machine
# The nodes will have 2 values (outedges, isTerminal: bool)
import time
from collections import deque

def getSafeStates(vertices, adj):
    def dfs(node):
        adjnodes = adj[node]
        visited[node][0] = 1
        for nextnode in adjnodes:
            if visited[nextnode][0] == 1:
                # This is a loop so this can't be a safenode
                break
            elif visited[nextnode][0] == 2:
                if not visited[nextnode][1]:
                    # If the nextnode is already completely visited and not a safenode, the node won't be a safe node either
                    break
            else:
                dfs(nextnode)
                if not visited[nextnode][1]:
                    break
        else:
            # If the node has all neighbouring nodes as safe nodes
            visited[node][1] = True
            safeNodes.append(node)
        visited[node][0] = 2
        

    safeNodes = deque()
    visited = {i:[0, False]for i in range(vertices)}
    for n_ in range(vertices):
        if adj[n_] == []:
            safeNodes.append(n_)
            # Since the node is a terminal node, there will be no out-edges.
            visited[n_][0] = 2
            # Mark it as a terminal or safe node as it has no out-edges
            visited[n_][1] = True

    #print(safeNodes)

    for vertice in range(vertices):
        if not visited[vertice][0]:
            #print(vertice)
            # If the vertice or node is not visited
            dfs(vertice)
    
    return sorted(list(safeNodes))

t1 = time.time()

adj = [[1,2],[2,3],[5],[0],[5],[],[]]
vertices = len(adj)
res = getSafeStates(vertices, adj)
t2 = time.time()
print(t2 - t1)
#print(res)