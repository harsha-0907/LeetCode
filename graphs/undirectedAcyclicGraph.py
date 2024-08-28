# To check if the graph has a cycle in it
import time


def isCycleBFS(v, adj):
    cnt = 0; queue = []
    not_visited = [i for i in range(v)]
    while not_visited != []:
        if cnt == len(queue):
            queue.append(not_visited[0])
        node = queue[cnt]; cnt += 1
        #print(node)
        not_visited.remove(node)
        nodes = adj[node]
        #print(node, nodes)
        for n in nodes:
            if n in not_visited:
                if n in queue:
                    # Cycle Exists
                    #print("Cycle Exists")
                    return True
                queue.append(n)
    return False


def recursiveDFS(v1, adj1):
    def dfs(node, prev):
        if node not in not_visited:
            return True
        adjnodes = adj1[node]; not_visited.remove(node)
        res = False
        for n in adjnodes:
            if n != prev:
                res = dfs(n, node) or res
                if res:
                    break
        return res
    
    not_visited = [i for i in range(v1)]
    res = False
    while not_visited != []:
        res = dfs(not_visited[0], None) or res
        if res:
            break
    return res
    
    

V, E = map(int, input().split())
adj = [[] for i in range(V)]
for _ in range(E):
	u1, v1 = map(int, input().split())
	adj[u1].append(v1)
	adj[v1].append(u1)
#v = 4
#adj = [[], [2], [1, 3], [2]]
print(adj)
print(recursiveDFS(v, adj))

"""
4 2
1 2
2 3
"""