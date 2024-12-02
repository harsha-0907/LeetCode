# Rotting Oranges


def findRottenOranges(matrix, m, n):
    spoilt = []; empty_cells = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                spoilt.append((i, j))
            if matrix[i][j] == 0:
                empty_cells += 1
    return spoilt, empty_cells

def isOutside(i, j):
    if i < 0 or i >= m:
        return True
    if j < 0 or j >= n:
        return True
    return False



def spreadRot(spoilt_nodes):
    list1 = []
    for node in spoilt_nodes:
        #print(node)
        (i, j) = node
        if not isOutside(i+1, j) and (i+1, j) not in visited and (i+1, j) not in list1 and matrix[i+1][j] != 0:
            list1.append((i+1, j))
        if not isOutside(i-1, j) and (i-1, j) not in visited and (i-1, j) not in list1 and matrix[i-1][j] != 0:
            list1.append((i-1, j))
        if not isOutside(i, j+1) and (i, j+1) not in visited and (i, j+1) not in list1 and matrix[i][j+1] != 0:
            list1.append((i, j+1))
        if not isOutside(i, j-1) and (i, j-1) not in visited and (i, j-1) not in list1 and matrix[i][j-1] != 0:
            list1.append((i, j-1))
    
    if list1 == []:
        return 0
    visited.extend(list1)
    return spreadRot(list1) + 1

matrix = [[0,2]]
m = len(matrix); n = len(matrix[0])

spoilt_nodes, empty_cells = findRottenOranges(matrix, m ,n)
visited = spoilt_nodes
#print(spoilt_nodes)
res = spreadRot(spoilt_nodes)
if (m * n) - empty_cells == len(spoilt_nodes):
    print(res)
    #return res
else:
    print('-1')
    #return -1
