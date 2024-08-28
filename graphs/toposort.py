# Toplogical-Sort

def createTopoSort(v, adj):
    # If there exists a topo-sort return the path, else return []
    def dfs(node, path):
        adjnodes = adj[node]
        for n in adjnodes:
            if n in path:
                # Loop exists
                return True
            res = dfs(n, path+[n])

        if node not in total_path:
            total_path.append(node)
            not_visited.remove(node)
    
    not_visited = [i for i in range(v)]
    total_path = []
    while not_visited != []:
        res = dfs(not_visited[0], [])
        if res:
            return []
    return total_path
    


