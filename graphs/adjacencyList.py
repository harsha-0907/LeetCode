# Create an adjacency list in python


def createAdjacencyList(v, edges):
    for i in range(v):
        dict1[i] = []
    
    for edge in edges:
        nodeA, nodeB = edge
        dict1[nodeA].append(nodeB)
        dict1[nodeB].append(nodeA)

    return dict1
dict1 = dict()
createAdjacencyList(v, edges)
ans =[]
for node in dict1:
    ans.append(dict1[node])

return ans