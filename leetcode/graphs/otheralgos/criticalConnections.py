# TO find the edges that break the graph to 2 if removed

# These are the edges that are not present in a loop

#Procedure:
# Run dfs in a graph, if there is a loop add all the nodes to that dfs.
# The nodes in the loop start fromm the node that triggered the visited to itself in a iteration.
# All the remaining nodes are those that are not in the loop

from collections import deque

def criticalConnection(n, edges):
        # Create an adjacency list
        adj = [[] for i in range(n)]
        for edge in edges:
            u_, v_ = edge
            adj[u_].append(v_)
            adj[v_].append(u_)
        
        visited = {i:0 for i in range(n)}; criticaledges = set()
        time = 1
        firstTime = dict()

        def dfs(node, parent, fC):
            # Lets mark the node as visited
            nonlocal time
            #print(node, fC)
            visited[node] = 1
            firstTime[node] = actualdist = fC
            adjnodes = adj[node]
            for nextnode in adjnodes:
                if nextnode == parent:
                    continue
                elif visited[nextnode] == 1:
                    actualdist = min(actualdist, firstTime[nextnode])
                    #print(node, nextnode, actualdist)
                    # This edge is not a critical edge
                else:
                    time += 1
                    actual = dfs(nextnode, node, time)
                    #print(actual > fC, actual, fC, node, nextnode)
                    if actual > fC:
                        criticaledges.add((node, nextnode))
                    else:
                        actualdist = min(actualdist, actual)
            
            print("Final ",node, actualdist)
            return actualdist
        
        dfs(0, None, time)

        #print(criticaledges, time)
        return criticaledges
n = 4
edges = [[0,1],[1,2],[2,0],[1,3]]

res = criticalConnection(n, edges)

print(res)