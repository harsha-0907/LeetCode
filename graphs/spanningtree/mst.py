# To calculate the sum of edges of a minimum spanning tree
import heapq

def mstWithEdges(n, edges):
    edges = sorted(edges, key= lambda x: x[2])
    #print(edges)
    visited = set()
    u_, v_, wt = edges[0]
    visited.add(u_); visited.add(v_); tot = wt
    for edge in edges[1:]:
        u_, v_, wt = edge
        if u_ not in visited:
            visited.add(u_)
            tot += wt
        elif v_ not in visited:
            visited.add(v_)
            tot += wt

    return tot

def mstWithAdj(n, adj):
    # MST with the given adjacency list
    src = 0
    heapq.heappush(queue, (0, 0, -1))   # (dist, nextnode, node)
    for i in range(n):
        for edge in adj[i]:
            heapq.heappush(queue, (edge[1], edge[0], i))
    
    tot = 0
    while queue:
        dist, nn, n = heapq.heappop()
        if nn not in visited:
            tot += dist
            visited.add(nn)
        elif n not in visited:
            tot += dist
            visited.add(n)
    
    return tot
n = 2
edges = [[0, 1, 5]]
res = mst(n, edges)
print(res)