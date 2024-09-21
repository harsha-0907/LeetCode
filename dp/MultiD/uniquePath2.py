# Unique Path-II (continution of UNique-Path-I)

def uniquePath2(grid):
    # Here there will be obstacles in the grids
    # The indexes with obstacles will have 0 ways
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0
    grid[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == 1:
                grid[i][j] = 0
            elif i == 0 or j == 0:
                if i == 0 and grid[0][j-1] == 0:
                    grid[0][j] = 0
                elif j == 0 and grid[i-1][0] == 0:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1   
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[m-1][n-1]

arr = [[0,0,0],[0,1,0],[0,0,0]]
res = uniquePath2(arr)

print(res)

