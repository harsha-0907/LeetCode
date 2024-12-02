# Kahn's Algorithm for Toposort using BFS
from collections import deque

def kahnAlgorithm(vertices, adj):
    # Let us convert the adjacency list from list to a dictionary
    def getEmptyNodes():
        list1 = []
        for i in dict1:
            if dict1[i] == []:
                list1.append(i)
        
        for i in list1:
            del(dict1[i])
        return list1

    # Convert the adj.list to a dictionary
    dict1 = {i:adj[i] for i in range(vertices)}
    print(dict1)

    total_path = []
    while dict1 != dict():
        list1 = getEmptyNodes()
        if list1 == []:
            return []
        for ele in dict1:
            for i in list1:
                if i in dict1[ele]:
                    dict1[ele].remove(i)
        print(list1, dict1)
        total_path = list1.extend(total_path)
    
    return list(reversed(total_path))


adj = [[], [], [3], [], [7, 5, 3], [6, 2, 1], [2], [6, 0]]
vertices = len(adj)
res = kahnAlgorithm(vertices, adj)
print(res)