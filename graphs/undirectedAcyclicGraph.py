# To check if the graph has a cycle in it


def isCycle(v, adj):
    cnt = 0; queue = []
    not_visited = [i for i in range(v)]
    while not_visited != []:
        if cnt == len(queue):
            queue.append(not_visited[0])
        node = queue[cnt]; cnt += 1
        #print(node)
        not_visited.remove(node)
        nodes = adj[node]
        print(node, nodes)
        for n in nodes:
            if n in not_visited:
                if n in queue:
                    # Cycle Exists
                    print("Cycle Exists")
                    return True
                queue.append(n)
    return False

v = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]

if isCycle(v, adj):
    print("Cycle exists")
else:
    print("No cycle exists")

"""
5 5
0 1
1 2
1 4
2 3
3 4
"""