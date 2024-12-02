# Find the shortest-path in a directed acyclic graph
from collections import deque

def shortestPath(vertices, edges, src):
    adj = [[] for i in range(vertices)]
    for edge in edges:
        u_, v_, wt_ = edge[0], edge[1], edge[2]
        adj[u_].append((v_, wt_))
    
    # The adjacency table is created
    #print(adj)

    src = 0 # Here the first element is always zero
    visited = set()
    total_distances = [-1 for i in range(vertices)]
    queue = deque([(src, 0)]); total_distances[0] = 0

    while queue != deque():
        node =queue.popleft()
        #print(node)
        adjnodes = adj[node[0]]
        #print(adjnodes)
        for nextnode in adjnodes:
            total = node[1] + nextnode[1]
            #print(total)
            if total_distances[nextnode[0]] != -1:
                if total < total_distances[nextnode[0]]:
                    total_distances[nextnode[0]] = total
                    queue.append((nextnode[0], total))
            else:
                #print("hi")
                total_distances[nextnode[0]] = total
                queue.append((nextnode[0], total))
    
    return total_distances

src = 0
vertices = 7
edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
print(shortestPath(vertices, edges, src))