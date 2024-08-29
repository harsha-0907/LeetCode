# Course-schedule-I

def courseSchedule(vertices, edges):
    adj = [[] for i in range(vertices)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
    
    def dfs(node):
        adjnodes = adj[node]
        visited.add(node)
        for n in adjnodes:
            if n in visited:
                return False
            if not dfs(n):
                return False
        visited.remove(node)
        path.add(node)
        return True
    
    path = set(); visited = set()
    for i in range(vertices):
        if i not in path:
            if not dfs(i):
                return False
    return True

def optimizedCanFinish(vertices, edges):
    adj = [[] for _ in range(vertices)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        
    visited = [0] * vertices  # 0: not visited, 1: visiting, 2: visited
        
    def dfs(node):
        if visited[node] == 1:
            return False  # cycle detected
        if visited[node] == 2:
            return True  # already visited
    
        visited[node] = 1
        for neighbor in adj[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 2
        return True
        
    for i in range(vertices):
        if not dfs(i):
            return False
    return True
edges = [[1,0]]
vertices = 2
print(optimizedCanFinish(vertices, edges))