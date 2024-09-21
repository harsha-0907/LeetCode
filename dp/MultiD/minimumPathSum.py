# To calculate the minimum sum path from one (0, 0) to (n-1, n-1)

def minimumSumPath(grid):
    m, n = len(grid), len(grid[0])
    sumarray = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                if j == 0:
                    # The first position can be achieved in grid[0][0] distance
                    sumarray[i][j] = grid[0][0]
                sumarray[i][j] = sumarray[i][j-1] + grid[i][j]
            elif j == 0:
                sumarray[i][j] = sumarray[i-1][j] + grid[i][j]
            else:
                sumarray[i][j] = min(sumarray[i-1][j], sumarray[i][j-1]) + grid[i][j]
    
    return sumarray[m-1][n-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]

res = minimumSumPath(grid)

print(res)