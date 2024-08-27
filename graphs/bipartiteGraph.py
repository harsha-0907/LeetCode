# Bi-partitie graph 
def biPartite(adj):
    """
    Here we are assigning the partition numbers to each vertex. Now we traverse through each node and get all the edges
    If a vertex is not yet added, add it and continue.
    If a vertex is not yet present, check if the vertex is present in the same partition -> If yes (return False)
    At last return True if there are no nodes present

    Improvments:
    Use deque for efficient ds. Use sets (for visited and others) to keep a track of nodes visited, (reduces time complexity)
    """
    not_visited = [i for i in range(len(adj))]
    queue = []; d1 = dict(); pos = 0
    while not_visited != []:
        queue.append(not_visited[0]); d1[not_visited[0]] = 0
        while pos < len(queue):
            node = queue[pos]; pos += 1
            mdirn = d1[node]; not_visited.remove(node)
            adjnodes = adj[node]
            for n in adjnodes:
                if n not in queue:
                    queue.append(n)
                    d1[n] = not mdirn
                elif d1[n] == d1[node]:
                    return False
    return True


graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
res = biPartite(graph)
print(res)