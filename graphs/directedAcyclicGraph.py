# Check if the graph contains cycles or not
def createAdjTable(vertices, edges):
    dict1 = {i: [] for i in range(vertices)}
    for edge in edges:
        dict1[edge[1]].append(edge[0])    
    return [dict1[i] for i in dict1]

def checkCycle(vertices, adj):
    return

edges = [[2,0],[2,1]]
vertices = 3
adj = createAdjTable(vertices, edges)
print(adj)
res = checkCycle(vertices, adj)
print(res)

