# Network Delay Time
from collections import deque

def calculateNetworkDelay(src, edges, n):
    # Here the signal needs to travel to all the nodes
    adj = [[] for i in range(n)]
    #k += 1
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
    queue = deque([(k, 0)])
    shortest_path = [float("inf") for i in range(n)]
    shortest_path[src] = 0

    while queue:
        node = queue.popleft()
        (pos, time) = node
        for nextnode in adj[pos]:
            time = time + nextnode[1]
            if time < shortest_path[nextnode[0]]:
                shortest_path[nextnode[0]] = time
                queue.append((nextnode[0], time))
    
    maxtime = 0
    for i in shortest_path:
        if i != float("inf"):
            if i > maxtime:
                maxtime = i
        else:
            # Not reachable 
            return -1
    
    return maxtime


n = 4
edges = [[2,1,1],[2,3,1],[3,4,1]]
src = 2

res = calculateNetworkDelay(src, edges, n)

print(res)
