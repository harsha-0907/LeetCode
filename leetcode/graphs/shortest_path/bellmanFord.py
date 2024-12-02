# To implement the bellman-ford algorithm 
import heapq

def bellmanFord(src, n, edges):
    adj = [[] for i in range(n)]
    for edge in edges:
        u_, v_, wt = edge
        adj[u_].append((v_, wt))
        #adj[v_].append((u_, wt)) -> only for undirected edge
    
    # To relax the edges
    shortest_paths = [float('inf') for i in range(n)]
    shortest_paths[src] = 0
    for i in range(n-1):
        for edge in edges:
            u_, v_, wt = edge
            dist = shortest_paths[u_] + wt
            if shortest_paths[v_] > dist:
                shortest_paths[v_] = dist
    #print(shortest_paths)

    # If one more round of relaxation is possibel then it is in negative cycle
    hasNegativeCycle = False
    for edge in edges:
        u_, v_, wt = edge
        dist = shortest_paths[u_] + wt
        if shortest_paths[v_] > dist:
            hasNegativeCycle = True
            break
        
    return hasNegativeCycle, shortest_paths

def dijkstras(src, n, edges):
    adj = [[] for i in range(n)]
    for edge in edges:
        u_, v_, wt = edge
        adj[u_].append((v_, wt))
    
    print(adj)
    queue = [(0, src)]
    shortest_paths = [float('inf') for i in range(n)]; shortest_paths[src] = 0

    while queue:
        node = heapq.heappop(queue)
        dist, pos = node
        adjnodes = adj[pos]
        for nextnode in adjnodes:
            npos, ndist = nextnode
            tot = dist + ndist
            if shortest_paths[npos] > tot:
                heapq.heappush(queue, (tot, npos))
                #queue.append((tot, npos))
                shortest_paths[npos] = tot
        
    return shortest_paths

src = 0
n = 6
edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
#res = bellmanFord(src, n, edges)
res = dijkstras(src, n, edges)

print(res)