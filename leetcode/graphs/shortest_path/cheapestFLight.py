# To find the cheapest flight within k stops
from collections import deque

def cheapestFlight(src, dest, edges, n, k):
    adj = [[] for i in range(n)]
    #k += 1
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
        
    shortest_path = [float("inf") for i in range(n)]
    queue = deque([(src, 0, 0)])

    while queue:
        node = queue.popleft()
        (pos, st, cost) = node; shortest_path[pos] = cost
        if st <=  k:
            # Can take more flights
            adjstops = adj[pos]
            for adjstop in adjstops:
                tot = cost + adjstop[1]
                if adjstop[0] == dest and shortest_path[dest] > tot:
                    shortest_path[dest] = tot
                elif shortest_path[adjstop[0]] > tot:
                    shortest_path[adjstop[0]] = tot
                    queue.append((adjstop[0], st+1, tot))
        
    if shortest_path[dest] == float("inf"):
        return -1
    return shortest_path[dest]

n = 3
k = 0
src = 0; dest = 2
edges =[[0,1,100],[1,2,100],[0,2,500]]

res = cheapestFlight(src, dest, edges, n, k)

print(res)