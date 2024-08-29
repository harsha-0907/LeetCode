# Check if the graph contains cycles or not
def createAdjTable(vertices, edges):
    dict1 = {i: [] for i in range(vertices)}
    for edge in edges:
        dict1[edge[1]].append(edge[0])    
    return [dict1[i] for i in dict1]

def checkCycle(vertices, adj):
    def dfs(node, path):
        adjnodes = adj[node]; r_ = False
        for n in adjnodes:
            if n in path:
                return True
            else:
                r_ = dfs(n, path+[n])
                if r_:
                    break
        if node not in total_path:
            total_path = [node] + path
            not_visited.remove(node)
        return r_

    not_visited = [i for i in range(vertices)]
    total_path = []
    while not_visited != []:
        r = dfs(not_visited[0], [not_visited[0]])
        if r:
            break
    else:
        # If the loop exits naturally, return the path
        return total_path
    
    # If the loop is terminated return empty list as there is a cycle
    return []

def isCyclic(vertices, adj):
    def dfs(node, visited):
        adjnodes = adj[node]
        visited.add(node)
        for n in adjnodes:
            if n in visited:
                return True
            if dfs(n, visited):
                return True
        visited.remove(node)
        visited1.add(node)
        return False

    visited1 = set()
    for i in range(vertices):
        if i not in visited1:
            if dfs(i, set()):
                return True

    return False

edges = [[1,0],[2,0],[3,1],[3,2]]
vertices = 4
adj = createAdjTable(vertices, edges)
print(adj)
#res = checkCycle(vertices, adj)
res = isCyclic(vertices, adj)
print(res)

"""
Here concept is if there is a cycle in the directed graph, the dependency can't be determined, so return [] if cycle is present

Procedure to obtain the path:
1. I know for sure that in the path the last node is the first course to be completed.
2. If I add the node at the first visit/traversal, it will be impossible to keep a track of the dependencies
3. Whereas if the course is added to the path from the end, we can be sure of the dependency
*4. The cycle doesn't depend on the total_path, rather it depends on the path for the chosen connected graph
5. The local path is never constant because if there is a loop it will be always identified, so no need to remeber the local path
6. The total_path is to be reversed at last of each connected component because the nodes are added at last,
 so we reversed to get the order of dependencies right.

"""