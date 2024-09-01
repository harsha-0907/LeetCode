# Shortest-path Algorithm for an undirected graph
# Time-Complexity : O(n^2)
# Space-Complexity : O(n^2)
from collections import deque

def dijkstras(n, adj, src):
    """
    In this algorithm we find the shortest path using the bfs algorithm
    """
    shortest_distances = [float("inf") for i in range(n)]
    parentnodes = [0 for i in range(n)]
    queue = deque([(src, 0)]); shortest_distances[src] = 0; empty = deque()
    while queue != empty:
        node = queue.popleft()
        adjnodes = adj[node[0]]
        for nextnode in adjnodes:
            total = node[1] + nextnode[1]
            if total < shortest_distances[nextnode[0]]:
                shortest_distances[nextnode[0]] = total
                queue.append((nextnode[0], total))
                parentnodes[nextnode[0]] = node[0]
    
    # Finding the shortedt path
    print(parentnodes)

    return shortest_distances

V = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
src = 2
res = dijkstras(V, adj, src)
print(res)