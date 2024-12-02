# Find the nearest 0 in the matrix for each & every position

def matrix01(matrix):
    def isOutside(i, j):
        if i < 0 or i >= m:
            return True
        if j < 0 or j >= n:
            return True
        return False
    
    zero1s = []; one1s = []
    m = len(matrix); n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if not isOutside(i+1, j) and matrix[i+1][j] == 0:
                    zero1s.append((i+1, j))
                    continue
                if not isOutside(i-1, j) and matrix[i-1][j] == 0:
                    zero1s.append((i-1, j))
                    continue
                if not isOutside(i, j+1) and matrix[i][j+1] == 0:
                    zero1s.append((i, j+1))
                    continue
                if not isOutside(i, j-1) and matrix[i][j-1] == 0:
                    zero1s.append((i, j-1))
                    continue
                one1s.append((i, j))
    
    print(one1s)
    print(zero1s)
    
    for zero1 in zero1s:
        for one1 in one1s:
            dist = abs(zero1[0] - one1[0]) + abs(zero1[1] - one1[1])
            if matrix[one1[0]][one1[1]] == 1:
                matrix[one1[0]][one1[1]] = dist
            else:
                matrix[one1[0]][one1[1]] = min(matrix[one1[0]][one1[1]], dist)

    return matrix

matrix = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
print(matrix01(matrix))