# Alien-Dictionary
from collections import deque

def createAdjList(words):
    adj = [[] for i in range(vertices)]
    for i in range(len(words)-1):
        w1 = words[i]; w2 = words[i+1]
        l = min(len(w1), len(w2))
        for i in range(l):
            if w1[i] != w2[i]:
                n1 = ord(w1[i]) - 97
                n2 = ord(w2[i]) - 97
                #print(n2, '->', n1)
                adj[n1].append(n2)
                break
    return adj


def createAlienGraph(vertices, words):
    def dfs(node):
        adjnodes = adj[node]; visited[node] = 1
        for nextnode in adjnodes:
            if visited[nextnode] == 1:
                # Loop exists
                return False
            elif visited[nextnode] == 2:
                continue
            else:
                if not dfs(nextnode):
                    return False
        
        visited[node] = 2
        print(node)
        total_path.appendleft(node)
        return True


    adj = createAdjList(words)
    #print(adj)
    total_path = deque()
    visited = {i:0 for i in range(vertices)}
    for i in range(vertices):
        if not visited[i]:
            if not dfs(i):
                return []
    
    return total_path

words = ["baa","abcd","abca","cab","cad"]
vertices = 4
res = createAlienGraph(vertices, words)
res = [chr(i + 97) for i in res]
print(res)