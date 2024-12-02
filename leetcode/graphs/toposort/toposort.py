# Toposort in graphs

def toposort(vertices, adj):
    def dfs(node, visited):
        #print(node)
        if node in topological_order:
            #print("Node is already visited", node)
            # The node is already visited, don't go again
            return None
        adjnodes = adj[node]; visited.add(node)
        #print(adjnodes, visited)
        
        for nextnode in adjnodes:
            if nextnode in visited:
                return True
            if dfs(nextnode, visited):
                return True
        
        if node not in topological_order:
            topological_order.append(node)
        #print(node)
        visited.remove(node)
        return None
    topological_order = []
    for i in range(vertices):
        if i not in topological_order:
            if dfs(i, set()):
                return []
    
    return topological_order

adj =  [[], [], [3], [], [7, 5, 3], [6, 2, 1], [2], [6, 0]]
vertices = len(adj)

res = toposort(vertices, adj)

print(res, "\n", list(reversed(res)))