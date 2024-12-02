# To calculate the sum of edges of a minimum spanning tree
import heapq
from typing import List

def convertToMST(n, adj) -> List[List[int, int]]:
    queue = [(0, 0, -1)]; tot = 0
    mst = []; visited = set()
    while queue:
        node = heapq.heappop(queue)
        wt, node, parent = node
        if node in visited:
            continue
        tot += wt
        if parent != -1:
            mst.append((parent, node))
            #print(wt)
        visited.add(node)
        adjnodes = adj[node]
        for nn in adjnodes:
            npos, wt1 = nn
            if npos not in visited:
                heapq.heappush(queue, (wt1, npos, node))
        
    return tot
