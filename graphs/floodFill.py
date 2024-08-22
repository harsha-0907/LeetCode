# Flood Fill - Leetcode

def isOutside(i, j):
    if i < 0 or i >= m:
        return True
    if j < 0 or j >= n:
        return True
    return False

def floodFill(filledNodes):
    list1 = []
    for node in filledNodes:
        (i, j) = node
        if not isOutside(i+1, j) and (i+1, j) not in list1 and matrix[i+1][j] != color and matrix[i+1][j] == starting_color:
            matrix[i+1][j] = color
            list1.append((i+1, j))
        if not isOutside(i-1, j) and (i-1, j) not in list1 and matrix[i-1][j] != color and matrix[i-1][j] == starting_color:
            matrix[i-1][j] = color
            list1.append((i-1, j))
        if not isOutside(i, j+1) and (i, j+1) not in list1 and matrix[i][j+1] != color and matrix[i][j+1] == starting_color:
            matrix[i][j+1] = color
            list1.append((i, j+1))
        if not isOutside(i, j-1) and (i, j-1) not in list1 and matrix[i][j-1] != color and matrix[i][j-1] == starting_color:
            matrix[i][j-1] = color
            list1.append((i, j-1))
        
    if list1 == []:
        return None
    return floodFill(list1)

matrix = [[0,0,0],[0,1,0]]
m = len(matrix); n = len(matrix[0])
sr = 1; sc = 1; color = 2
starting_color = matrix[sr][sc]
matrix[sr][sc] = color
floodFill([(sr, sc)])
print(matrix)