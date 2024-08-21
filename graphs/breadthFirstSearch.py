# Breadth-First-Search in a adjacency list representation of linked lists

def adjacencyList(v, adj):
    queue = [0]; cnt = 0
    while cnt < len(queue):
        node = queue[cnt]
        nodes = adj[node]
        for n in nodes:
            if n not in queue:
                queue.append(n)
        cnt += 1
    return queue


adj = [[1,2,3], [], [4], [], []]
v = 5
res = adjacencyList(v, adj)
print(res)