# Find the number of connected provinces

def findProvinces(isConnected):
    isConnected = convertMatrixToAdjacencyTable(isConnected)
    vertices = len(isConnected)
    not_visited = [i for i in range(vertices)]
    queue = [0]; cnt = 0
    provinces = 1
    while not_visited != []:
        if cnt == len(queue):
            provinces += 1
            queue.append(not_visited[0])
        node = queue[cnt]
        #print(node, provinces)
        cnt += 1
        not_visited.remove(node)
        adj_nodes = isConnected[node]
        for n in adj_nodes:
            if n not in queue:
                queue.append(n)
    return provinces

def findMatrixProvinces(matrix)    :
    queue = [0]; cnt = 0
    provinces = 1
    no_of_vertices = len(matrix)
    not_visited = [i for i in range(no_of_vertices)]
    while not_visited != []:
        if len(queue) == cnt:
            provinces += 1
            queue.append(not_visited[0])
    
        node = queue[cnt]; cnt += 1
        not_visited.remove(node)
        for n in range(len(matrix[node])):
            if matrix[node][n] == 1 and n not in queue:
                queue.append(n)
    
    return provinces


def convertMatrixToAdjacencyTable(matrix):
    # This works for both directed and undirected graph
    adj = []
    n = len(matrix)
    for i in range(n):
        l = []
        for j in range(n):
            if matrix[i][j] == 1:
                l.append(j)
        adj.append(l)
    return adj

matrix = [[1,1,0],[1,1,0],[0,0,1]]
#print(convertMatrixToAdjacencyTable(matrix))
res = findMatrixProvinces(matrix)
print(res)