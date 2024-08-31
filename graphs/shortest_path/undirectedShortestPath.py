# Shortest path in Undirected graph
from collections import deque
import time

def createAdjList(vertices, edges):
    adj = [[] for i in range(vertices)]
    for edge in edges:
        u_, v_ = edge[0], edge[1]
        adj[u_].append(v_)
        adj[v_].append(u_)
    return adj

def findShortestPath(vertices, src, edges):
    distances = [float("inf") for i in range(vertices)]
    queue = [src]; visited = set(); distance = 0
    adj = createAdjList(vertices, edges)
    
    while len(queue) != 0:
        list1 = deque()
        for node in queue:
            if node not in visited:
                distances[node] = distance
                adjnodes = adj[node]
                for nextnode in adjnodes:
                    if nextnode not in list1 and nextnode not in queue:
                        list1.append(nextnode)
            
            visited.add(node)
        queue = list1
        distance += 1

    return distances
t1 = time.time()
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
n = 9
src = 0
res = findShortestPath(n, src, edges)
print(time.time() - t1)
print(res)
