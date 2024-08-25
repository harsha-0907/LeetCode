# Find the surrounded region

# THis is kind of brute-force method solve in approx 2* O(n * m) -> Very Large
def getX(matrix):
    """
    Here the procedure taken is to find all the possible O's that are not in the boundary. And then checking if the
    group they are in are connected to any boundary element. If they are not connected they are stored seperately for 
    modification after finding all the nodes in the group. The time complexity is very high hence not optimal
    """
    m = len(matrix); n = len(matrix[0])
    nodes = []
    for i in range(1, m-1):
        for j in range(1, n-1):
            if matrix[i][j] == 'O':
                nodes.append((i, j))
    
    #print("Nodes ->", nodes)
    print("Complete")
    node_group = []; cnt = 0; hasBoundary = False; group= []
    while nodes != []:
        #if len(group) == m * n:
        if cnt == len(group):
            if group != []:
                if not hasBoundary:
                    # Only nodes that need to be replaced are added here
                    node_group.append(group)
            hasBoundary = False
            group = [nodes[0]]; cnt = 0
        
        node = group[cnt]; cnt += 1
        #print(node)
        nodes.remove(node)
        (i, j) = node
        if matrix[i-1][j] == 'O':
            if i-1 == 0:
                hasBoundary = True
            elif (i-1, j) not in group:
                group.append((i-1, j))
        if matrix[i+1][j] == 'O':
            if i+1 == m-1:
                hasBoundary = True
            elif (i+1, j) not in group:
                group.append((i+1, j))
        if matrix[i][j-1] == 'O':
            if j-1 == 0:
                hasBoundary = True
            elif (i, j-1) not in group:
                group.append((i, j-1))
        if matrix[i][j+1] == 'O':
            if j+1 == n-1:
                hasBoundary = True
            elif (i, j+1) not in group:
                #print("R")
                group.append((i, j+1))
    #print(group)
    if group != [] and not hasBoundary:
        node_group.append(group)
    #print(node_group)
    
    # The nodes that have no connection with outside - node_group
    
    for group in node_group:
        for pos in group:
            i, j = pos
            matrix[i][j] = 'X'
    
    return matrix

def surroundedRegions(matrix):
    """For example if  there is only one entry point and nodes are still being explored, we should wait
    till the group is completely explored so it is important to make sure that the group is also completely explored.
     i.e: (cnt != len(group))"""
    def isOutside(i, j):
        if i >= m or i < 0 or j < 0 or j >= n:
            return True
        return False
            
    m = len(matrix); n = len(matrix[0])
    nodes = []
    for i in range(m):
        if matrix[i][0] == 'O':
            nodes.append((i, 0))
        if matrix[i][n-1] == 'O':
            nodes.append((i, n-1))
        
    for i in range(1, n-1):
        if matrix[0][i] == 'O':
            nodes.append((0, i))
        if matrix[m-1][i] == 'O':
            nodes.append((m-1, i))
    #print(nodes)
    group = []; cnt = 0
    while nodes != [] or cnt != len(group):
        if cnt == len(group):
            group = [nodes[0]]; cnt = 0
        node = group[cnt]; cnt += 1
        i, j = node
        #print(node, group)
        if node in nodes:
            nodes.remove(node)
        matrix[i][j] = 'S'
        if not isOutside(i+1, j) and matrix[i+1][j] == 'O' and (i+1, j) not in group:
            group.append((i+1, j))
        if not isOutside(i-1, j) and matrix[i-1][j] == 'O' and (i-1, j) not in group:
            group.append((i-1, j))
        if not isOutside(i, j+1) and matrix[i][j+1] == 'O' and (i, j+1) not in group:
            group.append((i, j+1))
        if not isOutside(i, j-1) and matrix[i][j-1] == 'O' and (i, j-1) not in group:
            group.append((i, j-1))

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'S':
                matrix[i][j] = 'O'
            else:
                matrix[i][j] = 'X'
        
    return matrix


matrix = [["O","O","O"],["O","O","O"],["O","O","O"]]

print(len(matrix), len(matrix[0]))
matrix1 = surroundedRegions(matrix)

print(matrix1)
